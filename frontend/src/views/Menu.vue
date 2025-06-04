<script setup>
import { ref, onMounted } from 'vue'
import Api from '../utils/Api'
import Button from '../components/Button.vue'
import MatIcon from '../components/MatIcon.vue'
import Product from '../components/Product.vue'
import { Toast, useToast } from 'primevue'
import useAuthStore from '../store/auth'

const api = Api.access()
const products = ref([])
const toast = useToast()
const authStore = useAuthStore()

onMounted(async () => {
  api.get("/products")
    .then(data => {
      products.value = data
    })
    .catch(error => {
      toast.add({ summary: "Unexpected error", detail: "There was an unexpected error", severity: 'error' })
    })
})

const buyProduct = async product => {
  api.post('/orders', { product: product, user_id: authStore.user.id })
    .then(data => {
      toast.add({
        summary: "Info",
        detail: "Serving product...",
        severity: 'info',
        group: 'bl',
        life: 3000
      })
    })
    .catch(error => {
      toast.add({
        summary: "Error",
        detail: "There was an error doing de order",
        group: 'bl',
        severity: 'error'
      })
    })
}
</script>

<template>
  <Toast />
  <div class="py-10 px-4 flex flex-col gap-15">
    <h2 class="text-center text-6xl mb-4">SELECCIONA UN PRODUCTO</h2>
    <h3 class="text-center text-2xl">Selecciona un producto para poder selecciona un producto, Selecciona un producto para poder selecciona</h3>
  </div>
  <div class="w-full py-10 bg-gazpacho">
    <div v-if="products.length" class="m-15 grid grid-cols-1 sm:grid-cols-3 gap-6">
      <Product
        v-for="product in products"
        v-bind="product"
        :key="product.id"
        :buy-callback="buyProduct"
      />
    </div>
    <div v-else class="h-full flex flex-col gap-2 items-center">
      <mat-icon class="animate-spin !text-3xl">progress_activity</mat-icon>
      <span class="text-xl">Loading...</span>
    </div>
  </div>
</template>
