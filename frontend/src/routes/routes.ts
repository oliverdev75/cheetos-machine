import Home from '../views/Home.vue'
import About from '../views/About.vue'

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
    }
]