import { getConfig } from "@/env"

const config = getConfig()

export class ApiClient {

    async get<T>(url: string): Promise<T> {

        const response = await fetch(config.API_URL + url)

        if (!response.ok) {
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
        })

        if (!response.ok) {
            throw new Error(response.statusText)
        }

        return response.json() as Promise<T>
    }
}

export const api = new ApiClient()