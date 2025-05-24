<script setup>
import { ref, onMounted } from 'vue'
import useApi from '../composables/api'

const api = useApi()
const products = ref([])

onMounted(async () => {
  try {
    products.value = await api.get("/product")
    console.log(products.value)
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Carta | Nuestros Productos</h2>
    <div class="m-15 grid grid-cols-1 sm:grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-6">
      <article
        v-for="product in products"
        :key="product.id"
        class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-200"
      >
        <img
            :src="product.image"
            alt="Imagen del product"
            class="m-auto h-60 object-cover"
        />
        <div class="p-4">
          <h3 class="text-lg font-semibold mb-2">{{ product.name }}</h3>
          <p class="text-gray-600 text-sm">$ {{ product.price.toFixed(2) }}</p>
        </div>
      </article>
    </div>
  </div>
</template>
