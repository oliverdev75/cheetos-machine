import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Admin from '../views/Admin/Admin.vue'
import Orders from '../views/Orders.vue'
import Dashboard from '../views/Dashboard.vue'

const requiresLogged = () => {
    
}

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

        name: 'login',
        path: '/login',
        component: Login,
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
        name: 'orders',
        path: '/orders',
        component: Orders,

    }
]