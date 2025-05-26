import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Dashboard from '../views/Dashboard.vue'
import Admin from '../views/Admin/Admin.vue'
import Menu from '../views/Menu.vue'
import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
import Orders from '../views/Orders.vue'


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

        name: 'account',
        path: '/account',
        component: Account,
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

        name: 'menu',
        path: '/carta',
        component: Menu,

    },
    {

        name: 'orders',
        path: '/orders',
        component: Orders,

    }
]