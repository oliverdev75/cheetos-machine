import axios from "axios"
import { API_URL } from "../constants/api"

export default function useApi() {
    const client = axios.create({
        baseURL: API_URL,
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

    const createPromise = (req: any) => {
        return new Promise(async (resolve, reject) => {
            try {
                const res = await req()
                resolve(res.data)
            } catch (error) {
                reject(error)
            }
        })
    }

    const makeParams = (params: object | undefined) => {
        let urlParams = "?"
        const paramNames = params ? Object.keys(params) : []
        const paramValues = params ? Object.values(params) : []

        for (let i = 0; i < paramNames.length; i++) {
            urlParams += paramNames[i] + '='
            urlParams += paramValues[i] + '&'
        }

        return urlParams.substring(0, urlParams.length)
    }

    const get = async (url: string, params?: any) => {
        return createPromise(() => client.get(url + makeParams(params)))
    }

    const post = async (url: string, data: any, params?: object) => {
        return createPromise(() => client.post(url + makeParams(params), data))
    }

    const put = async (url: string, data: any, params?: object) => {
        return createPromise(() => client.put(url + makeParams(params), data))
    }

    const del = async (url: string, params?: object) => {
        return createPromise(() => client.delete(url + createPromise(params)))
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