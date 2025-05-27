import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Dashboard from '../views/Dashboard.vue'
import Admin from '../views/Admin/Admin.vue'
import Menu from '../views/Menu.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Account from '../views/Account.vue'
import Orders from '../views/Orders.vue'
import useAuthStore from '../store/auth'


const requireAuth = (_to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.authToken
    if (!token) {
        next({ name: 'login' })
    } else {
        next()
    }
}

const requireAdmin = (to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.authToken
    if (!token) {
        next({ name: 'login' })
    } else {
        const user = authStore.user
        if (user.roles && user.roles.includes('admin')) {
            next()
        } else {
            next('/')
        }
    }
}

const requireGuest = (_to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.authToken
    if (token) {
        next('/')
    } else {
        next()
    }
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
        beforeEnter: requireGuest,
        component: Login,
    },
    {

        name: 'register',
        path: '/register',
        beforeEnter: requireGuest,
        component: Register,
    },
    {
        name: 'account',
        path: '/account',
        beforeEnter: requireAuth,
        component: Account,
    },
    {
        name: 'admin',
        path: '/admin',
        beforeEnter: requireAdmin,
        component: Admin,
    },
    {

        name: 'menu',
        path: '/carta',
        beforeEnter: requireAuth,
        component: Menu,
    },
    {
        name: 'orders',
        path: '/orders',
        beforeEnter: requireAuth,
        component: Orders,

    }
]