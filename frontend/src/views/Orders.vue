<script setup lang="ts">
import { onMounted, ref } from 'vue'
import useOrders from '../composables/useOrders'
import useLogin from '../composables/useAuth'

const { getUserIdFromToken } = useLogin();
const { getOrders, createOrder, deleteOrder, checkLastOrderDeliverDate, deliverLastOrder } = useOrders()
const orders = ref([])

const userId = ref<number | null>(null)

onMounted(async () => {
  const token = localStorage.getItem('authToken')
  if (token) {
    userId.value = getUserIdFromToken(token)
  }

  orders.value = await getOrders()
  checkLastOrderDeliverDate(userId.value);
})

const newOrder = async () => {
  const res = await createOrder(userId.value, 19.99, [1, 2])
  console.log('Pedido creado:', res)
  orders.value = await getOrders()
}


const removeOrder = async (id: number) => {
  await deleteOrder(id)
  orders.value = await getOrders()
}

const deliver = async () => {
  try {
    const res = await deliverLastOrder(1)
    console.log('Pedido entregado:', res)
    orders.value = await getOrders()  // refresca la lista
  } catch (e) {
    console.error(e)
  }
}

</script>

<template>
  <h1>Pedidos</h1>
  <button @click="newOrder">Crear pedido</button>
  <button @click="deliver">Deliver</button>

  <ul>
    <li v-for="order in orders" :key="order.id">
      ID: {{ order.id }} | Precio: {{ order.price }}€ | Deliver: {{ order.delivered_at }}
    </li>
  </ul>
</template>
