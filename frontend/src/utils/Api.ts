import type { AxiosInstance } from "axios"
import axios from "axios"
import { API_URL } from "../constants/api"


class Api {

    token: string | null = null

    private static instance: Api | null = null

    private constructor() {
    }

    static access() {
        return this.instance || (this.instance = new Api())
    }

    setAuthToken(token: string | null = null) {
        if (!token) {
            this.token = null
        }

        this.token = token
    }

    createPromise(req: () => Promise<any>): Promise<any> {
        console.log("Auth: ", localStorage.getItem('authToken'))
        return new Promise<any>(async (resolve, reject) => {
            try {
                const res = await req()
                resolve(res.data)
            } catch (error) {
                reject(error)
            }
        })
    }

    makeParams(params: object | undefined): string {
        let urlParams = params ? "?" : ""
        const paramNames = params ? Object.keys(params) : []
        const paramValues = params ? Object.values(params) : []

        for (let i = 0; i < paramNames.length; i++) {
            urlParams += paramNames[i] + '='
            urlParams += paramValues[i] + '&'
        }

        return urlParams.substring(0, urlParams.length)
    }

    authorizeRequest(): object {
        const token = localStorage.getItem('authToken')
        return token ? {
            headers: {
                Authorization: token ? `Bearer ${token}` : ''
            }
        } : {}
    }

    async get(url: string, params?: any): Promise<any> {
        const config = this.authorizeRequest()

        return this.createPromise(() => axios.get(API_URL + url + this.makeParams(params), config))
    }

    async post(url: string, data: any, params?: object): Promise<any> {
        const config = this.authorizeRequest()
        return this.createPromise(() => axios.post(API_URL + url + this.makeParams(params), data, config))
    }

    async put(url: string, data: any, params?: object): Promise<any> {
        const config = this.authorizeRequest()
        return this.createPromise(() => axios.put(API_URL + url + this.makeParams(params), data, config))
    }

    async delete(url: string, params?: object): Promise<any> {
        const config = this.authorizeRequest()
        return this.createPromise(() => axios.delete(API_URL + url + this.makeParams(params), config))
    }
}

export default Api