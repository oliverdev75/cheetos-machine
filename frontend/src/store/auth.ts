import { defineStore } from 'pinia'
import { ref } from 'vue'
import Api from '../utils/Api'

const useAuthStore = defineStore('auth', () => {
    const token = ref<string | null>(localStorage.getItem('authToken'))
    const user = ref(JSON.parse(localStorage.getItem('user') ?? '{}'))

    const setToken = (authToken: string) => {
        token.value = authToken
        localStorage.setItem('authToken', authToken)
        Api.access().setAuthToken(authToken)
    }

    const setUser = (authedUser: object) => {
        user.value = authedUser
        localStorage.setItem('user', JSON.stringify(user.value))
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
        setUser,
        removeToken
    }
})

export default useAuthStore