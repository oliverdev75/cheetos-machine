import axios from "axios"

export default function useApi() {
    const client = axios.create({
        baseURL: import.meta.env.VITE_API_URL,
        headers: {
            "Content-Type": "application/json",
        },
    })

    const setAuthToken = (token: string) => {
        if (token) {
            client.defaults.headers.common["Authorization"] = `Bearer ${token}`
        } else {
            delete client.defaults.headers.common["Authorization"]
        }
    }

    const get = async (url: string, params?: any) => {
        try {
            const res = await client.get(url, { params })
            return res.data
        } catch (error) {
            console.error("API GET error:", error)
            throw error
        }
    }

    const post = async (url: string, data: any) => {
        try {
            const res = await client.post(url, data)
            return res.data
        } catch (error) {
            console.error("API POST error:", error)
            throw error
        }
    }

    const put = async (url: string, data: any) => {
        try {
            const res = await client.put(url, data)
            return res.data
        } catch (error) {
            console.error("API PUT error:", error)
            throw error
        }
    }

    const del = async (url: string) => {
        try {
            const res = await client.delete(url)
            return res.data
        } catch (error) {
            console.error("API DELETE error:", error)
            throw error
        }
    }

    return {
        client,
        setAuthToken,
        get,
        post,
        put,
        del,
    }
}