import { useRouter } from "vue-router"
import Api from "../utils/Api"
import useAuthStore from "../store/auth"

export default function useAuth() {
    const api = Api.access()
    const router = useRouter()
    const authStore = useAuthStore()

    const login = async (email: string, password: string) => {
        await api.post("/login", { email, password })
            .then((data: any) => {
                // Guarda el token
                authStore.setToken(data.token)
                console.log(data.user)
                authStore.setUser(data.user)
ç
                router.push({ name: 'menu' })
            })
    }

    const logout = async () => {
        authStore.removeToken()
        authStore.user = null
        router.push({ name: 'login' })
    }

    const getUser = async () => {
        const token = authStore.token
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
        logout,
        getUser
    }
}
