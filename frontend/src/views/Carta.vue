<script setup>
import { ref, onMounted } from 'vue';
import useApi from '../composables/api';

const api = useApi();
const productos_carta = ref([]);

const obtenerProductos = async () => {
  try {
    productos_carta.value = await api.get("/product");
    console.log(productos_carta.value);
  } catch (error) {
    console.error(error);
  }
};

onMounted(obtenerProductos);
</script>

<template>
  <div class="p-4">
    <h2 class="text-2xl font-bold mb-4">Carta</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
      <div
        v-for="producto in productos_carta"
        :key="producto.id"
        class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-200"
      >
        <img
          :src="producto.image"
          alt="Imagen del producto"
          class="w-full h-48 object-cover"
        />
        <div class="p-4">
          <h3 class="text-lg font-semibold mb-2">{{ producto.name }}</h3>
          <p class="text-gray-600 text-sm">$ {{ producto.price.toFixed(2) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
