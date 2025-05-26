import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routes'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'

createApp(App)
    .use(router)
    .use(PrimeVue, {
        them: {
            preset: Aura
        }
    })
    .mount('#app')
