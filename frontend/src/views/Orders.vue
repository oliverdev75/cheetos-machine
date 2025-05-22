<script setup lang="ts">
import { onMounted, ref } from 'vue'
import useOrders from '../composables/useOrders'

const { getOrders, createOrder, deleteOrder } = useOrders()
const orders = ref([])

onMounted(async () => {
    orders.value = await getOrders()
})

const newOrder = async () => {
  const res = await createOrder(1, 19.99, [1, 2])
  console.log('Pedido creado:', res)
  orders.value = await getOrders()
}


const removeOrder = async (id: number) => {
    await deleteOrder(id)
    orders.value = await getOrders()
}
</script>

<template>
  <h1>Pedidos</h1>
  <button @click="newOrder">Crear pedido</button>

  <ul>
    <li v-for="order in orders" :key="order.id">
      ID: {{ order.id }} | Precio: {{ order.price }}€
      <button @click="removeOrder(order.id)">Eliminar</button>
    </li>
  </ul>
</template>
