<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Button from '../components/Button.vue'
import Api from '../utils/Api'
import { useRoute, useRouter } from 'vue-router'
import useAuthStore from '../store/auth'
import { useToast, Toast } from 'primevue'
import { API_URL } from '../constants/api'
import { errorMessages } from 'vue/compiler-sfc'

const api = Api.access()
const authStore = useAuthStore()
const route = useRoute()
const router = useRouter()
const toast = useToast()
const product = ref()

onMounted(() => {
    api.get(`/products/${route.params.id}`)
    .then(data => {
        product.value = data
    })
    .catch(error => {
        console.error(error)
    })
})

const buyProduct = async () => {
  api.post('/orders', { product: product.value })
    .then(async () => {
      toast.add({
        summary: "Info",
        detail: "Serving product...",
        severity: 'info',
        life: 3000
      })
      
      setTimeout(() => {
        router.push({ name: 'menu' })
      }, 5000)
    })
    .catch(() => {
      toast.add({
        summary: "Error",
        detail: "There was an error doing de order",
        severity: 'error'
      })
    })
/*     toast.add({
        summary: "Info",
        detail: "Serving product...",
        severity: 'info',
        group: 'bl',
        life: 3000
    })
      setTimeout(() => {
        router.push({ name: 'menu' })
      }, 5000) */
}

</script>

<template>
    <Toast />
    <div class="orange-background flex-1 w-full flex justify-center relative">
        <router-link :to="{ name: 'menu' }">
            <Button icon="arrow_back" white class="absolute left-5 top-5 px-5 py-2 shadow-lg">Volver</Button>
        </router-link>
        <div class="bg-white px-4 lg:px-0 lg:w-[70%] py-10 h-full flex flex-col items-center">
            <h2 class="text-6xl mb-3">FINALIZAR PEDIDO</h2>
            <h3 class="inline-block text-3xl text-neutral-400 mb-2">Canjea el token para dispensar el producto.</h3>
            <div class="orange-background my-5 size-95 flex flex-col justify-center items-center rounded-full">
                <img class="size-52 mb-5 object-contain" :src="API_URL + `/products/image/${product?.id}`" :alt="`${product?.name} image`">
                <h4 class="text-shadow-md text-white text-3xl text-center text-pretty">{{ product?.name }}</h4>
            </div>
            <Button class="text-5xl" @click="buyProduct">CANJEAR TOKEN</Button>
        </div>
    </div>
</template>

<style scoped>

.orange-background {
    background: url('/images/orange_background.jpg');
    background-repeat: repeat;
}

</style>