<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import useOrders from '../composables/useOrders'
import useLogin from '../composables/useAuth'

const router = useRouter()
const { getUser } = useLogin()
const { getOrders, createOrder, deleteOrder, checkLastOrderDeliverDate, deliverLastOrder } = useOrders()

const orders = ref([])
const user = ref()

onMounted(async () => {
  console.log("InMounted")
  user.value = await getUser()

  orders.value = await getOrders()
  await checkLastOrderDeliverDate(user.value?.id)
})



const newOrder = async () => {
  console.log("user.value?")
  console.log(user.value)
  const res = await createOrder(user.value?.id, 19.99, [1, 2])
  console.log('Pedido creado:', res)
  orders.value = await getOrders()
}

const removeOrder = async (id: number) => {
  await deleteOrder(id)
  orders.value = await getOrders()
}

const deliver = async () => {
  try {
    const res = await deliverLastOrder(user.value?.id)
    console.log('Pedido entregado:', res)
    orders.value = await getOrders()
  } catch (e) {
    console.error(e)
  }
}
</script>


<template>
  <h1>User</h1>
  <p>Email:</p>
  <h1>Pedidos</h1>
  <button @click="newOrder">Crear pedido</button>
  <button @click="deliver">Deliver</button>

  <ul>
    <li v-for="order in orders" :key="order.id">
      ID: {{ order.id }} | Precio: {{ order.price }}€ | Deliver: {{ order.delivered_at }}
    </li>
  </ul>
</template>
