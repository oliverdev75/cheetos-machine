import { createApp } from 'vue'
import './style.css'
import './home.css'
import App from './App.vue'
import router from './routes'

createApp(App).use(router).mount('#app')
