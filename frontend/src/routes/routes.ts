import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Dashboard from '../views/Dashboard.vue'
import Admin from '../views/Admin/Admin.vue'
import Menu from '../views/Menu.vue'
import BuyProduct from '../views/BuyProduct.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Account from '../views/Account.vue'
import Orders from '../views/Orders.vue'
import useAuthStore from '../store/auth'


const requireAuth = (_to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.token
    if (!token) {
        next({ name: 'login' })
    } else {
        next()
    }
}

const requireAdmin = (to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.token
    if (!token) {
        next({ name: 'login' })
    } else {
        const user = authStore.user
        if (!user) {
            next({ name: 'login' })
        }
        
        if (user.roles && user.roles.includes('admin')) {
            next()
        } else {
            next('/')
        }
    }
}

const requireGuest = (_to: any, _from: any, next: any) => {
    const authStore = useAuthStore()

    const token = authStore.token
    console.log('Token: ', token)
    if (token) {
        next({ name: 'menu' })
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
        component: Login,
        beforeEnter: requireGuest,
    },
    {

        name: 'register',
        path: '/register',
        component: Register,
        beforeEnter: requireGuest,
    },
    {
        name: 'account',
        path: '/account',
        component: Account,
        beforeEnter: requireAuth,
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
        component: Menu,
    },
    {
        name: 'buy-product',
        path: '/buy/:id',
        beforeEnter: requireAuth,
        component: BuyProduct,
    },
    {
        name: 'orders',
        path: '/orders',
        component: Orders,
        beforeEnter: requireAuth,

    }
]