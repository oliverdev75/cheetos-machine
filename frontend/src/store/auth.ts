import { defineStore } from 'pinia'
import { ref } from 'vue'

const useAuthStore = defineStore('auth', () => {
    const authToken = ref<string | null>(localStorage.getItem('authToken'))
    const user = ref()

    const setAuthToken = (token: string) => {
        authToken.value = token
        localStorage.setItem('authToken', token)
    }

    const removeAuthToken = () => {
        authToken.value = null
        localStorage.removeItem('authToken')
    }

    return {
        authToken,
        user,
        setAuthToken,
        removeAuthToken
    }
})

export default useAuthStore