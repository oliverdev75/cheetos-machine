import { defineStore } from 'pinia'
import { ref } from 'vue'
import Api from '../utils/Api'

const useAuthStore = defineStore('auth', () => {
    const token = ref<string | null>(localStorage.getItem('authToken'))
    const user = ref()

    const setToken = (authToken: string) => {
        token.value = authToken
        localStorage.setItem('authToken', authToken)
        Api.access().setAuthToken(authToken)
    }

    const removeToken = () => {
        token.value = null
        localStorage.removeItem('authToken')
        Api.access().setAuthToken()
    }

    return {
        token,
        user,
        setToken,
        removeToken
    }
})

export default useAuthStore