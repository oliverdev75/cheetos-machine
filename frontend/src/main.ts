import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './routes'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import { ToastService } from 'primevue'
import './style.css'
import 'primeicons/primeicons.css'

createApp(App)
    .use(createPinia())
    .use(router)
    .use(PrimeVue, {
        theme: {
            preset: Aura
        }
    })
    .use(ToastService)
    .mount('#app')
