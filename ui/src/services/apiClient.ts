import { getConfig } from "@/env"
import { useMessageStore } from "@/stores/message"

const config = getConfig()

export class ApiClient {

    async get<T>(url: string): Promise<T> {

        const response = await fetch(config.API_URL + url)

        if (!response.ok) {
            useMessageStore().addMessage(`API request failed for endpoint ${url}: ${response.statusText}`, 'error')
            throw new Error(response.statusText)
        }

        return response.json() as Promise<T>
    }

    async post<T>(url: string, body: unknown): Promise<T> {

        const response = await fetch(config.API_URL + url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        }).catch(error => {
            useMessageStore().addMessage(`API Post failed for endpoint ${url}: ${error}`, 'error')
            throw new Error(error)
        })

        if (!response.ok) {
            useMessageStore().addMessage(`API Post failed for endpoint ${url}: ${response.statusText}`, 'error')
            throw new Error(response.statusText)
        }

        return response.json() as Promise<T>
    }
}

export const api = new ApiClient()
