import { useRouter } from "vue-router"
import useApi from "./api"
import useAuthStore from "../store/auth"

export default function useAuth() {
    const api = useApi()
    const router = useRouter()
    const authStore = useAuthStore()

    const login = async (email: string, password: string) => {
        api.post("/login", { email, password })
            .then((data: any) => {
                // Guarda el token
                authStore.setAuthToken(data.token)
                authStore.user = data.user

                // Setea el token para futuras peticiones
                api.setAuthToken(data.token)
                router.push({ name: 'menu' })
            })
    }

    const getUser = async () => {
        const token = authStore.authToken
        if (!token) 
            return null

        const email = authStore.user?.email
        let user = null
        console.log(email)

        await api.get(`/user?email=${email}`)
            .then((response: any) => {
                user = response
            })
            .catch((error: any) => {
                console.error("Error decoding token or fetching user:", error)
                return null
            })

        return user
    }


    return {
        login,
        getUser
    }
}
