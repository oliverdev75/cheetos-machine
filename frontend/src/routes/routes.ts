import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Dashboard from '../views/Dashboard.vue'
import Admin from '../views/Admin/Admin.vue'
import Carta from '../views/Carta.vue'

export default [
    {
        name: 'home',
        path: '/',
        component: Home,
    },
    {
        name: 'about',
        path: '/about',
        component: About,
    },
    {
        name: 'dashboard',
        path: '/dashboard',
        component: Dashboard,
    },
    {
        name: 'admin',
        path: '/admin',
        component: Admin,
    },
    {
        name: 'carta',
        path: '/carta',
        component: Carta,
    }
]