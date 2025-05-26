<script setup>
import { ref, onMounted } from 'vue'
import useApi from '../composables/api'
import Button from '../components/Button.vue'
import MatIcon from '../components/MatIcon.vue'

const api = useApi()
const products = ref([])

onMounted(async () => {
  try {
    products.value = await api.get("/products")
    console.log(products.value)
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="py-10 px-4 flex flex-col gap-15">
    <h2 class="text-center text-6xl mb-4">SELECCIONA UN PRODUCTO</h2>
    <h3 class="text-center text-2xl">Selecciona un producto para poder selecciona un producto, Selecciona un producto para poder selecciona</h3>
  </div>
  <div class="w-full py-10 bg-gazpacho">
    <div v-if="products.length" class="m-15 grid grid-cols-1 sm:grid-cols-3 gap-6">
      <article
        v-for="product in products"
        :key="product.id"
        class="flex flex-col"
      >
        <img
            :src="product.image"
            alt="Imagen del product"
            class="m-auto h-60 object-cover"
        />
        <div class="w-full flex flex-col gap-3 items-center">
          <strong class="text-white text-center text-4xl text-shadow-lg">{{ product.name }}</strong>
          <Button icon="add_circle" white class="px-5 py-3 text-3xl gap-7" icon-class="!text-4xl">{{ product.price.toFixed(2).replace('.', ',') }}€</Button>
        </div>
      </article>
    </div>
    <div v-else class="h-full flex flex-col gap-10 items-center">
      <mat-icon class="!text-3xl">progress_activity</mat-icon>
      <span class="text-xl">Loading...</span>
    </div>
  </div>
</template>
