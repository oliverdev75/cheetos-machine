<template>
  <div>
    <h2>Orders</h2>

    <!-- Formulario para crear orden -->
    <form @submit.prevent="handleSubmit">
      <input v-model.number="form.user_id" type="number" placeholder="User ID" required />
      <input v-model.number="form.price" type="number" step="0.01" placeholder="Total Price" required />
      <button type="submit">Create Order</button>
    </form>

    <table class="table-auto w-full border border-gray-300 border-collapse">
      <thead>
        <tr>
          <th>ID</th>
          <th>User ID</th>
          <th>Price</th>
          <th>Created At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.id }}</td>
          <td>{{ order.user_id }}</td>
          <td>{{ order.price }}</td>
          <td>{{ formatDate(order.created_at) }}</td>
          <td>
            <button @click="deleteOrder(order.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Api from '../../utils/Api'

const api = Api.access()

const orders = ref([])
const form = ref({ user_id: '', price: '' })

// Obtener todas las órdenes
const fetchOrders = async () => {
  try {
    orders.value = await api.get('/orders')
  } catch (error) {
    console.error(error)
  }
}

onMounted(fetchOrders)

// Crear nueva orden
const handleSubmit = async () => {
  try {
    await api.post('/orders', form.value)
    await fetchOrders()
    resetForm()
  } catch (error) {
    console.error(error)
  }
}

// Borrar orden
const deleteOrder = async (id) => {
  if (!confirm('Are you sure you want to delete this order?')) return
  try {
    await api.del(`/orders/${id}`)
    await fetchOrders()
  } catch (error) {
    console.error(error)
  }
}

// Reset formulario
const resetForm = () => {
  form.value = { user_id: '', price: '' }
}

// Formatear fecha
const formatDate = (datetimeString) => {
  return new Date(datetimeString).toLocaleString()
}
</script>

<style scoped>
table, td, th {
    border: 2px solid black;
    padding: 10px;

    border-collapse: collapse;

    margin: 10px;
}
</style>