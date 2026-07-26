interface AppConfig {
    API_URL: string
    APP_NAME: string
}

declare global {
    interface Window {
        __APP_CONFIG__: AppConfig
    }
}

// This is a workaround to get the environment variables from the window object, since Vite does not support dynamic environment variables at runtime.
export function getConfig(): Readonly<AppConfig> {
    return window.__APP_CONFIG__ ? window.__APP_CONFIG__ : {API_URL: import.meta.env.VITE_API_URL, APP_NAME: import.meta.env.VITE_APP_NAME} as AppConfig
}
