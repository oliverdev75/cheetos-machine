import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Dashboard from '../views/Dashboard.vue'

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
    }
]