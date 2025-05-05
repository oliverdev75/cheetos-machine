import { createWebHistory , createRouter } from "vue-router"
import HelloWorld from "../components/HelloWorld.vue"
import Dashboard from "../components/Dashboard.vue"

const routes = [
    {
        path: '/',
        name: 'home',
        component: HelloWorld
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: Dashboard
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router