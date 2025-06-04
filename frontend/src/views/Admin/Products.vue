<template>
  <div>
    <h2>Products</h2>

    <!-- Formulario para crear/editar -->
    <form @submit.prevent="handleSubmit">
      <input v-model="form.name" placeholder="Product Name" required />
      <input v-model.number="form.price" type="number" step="0.01" placeholder="Price" required />
      <input v-model="form.image" placeholder="Image URL" required />
      <button type="submit">{{ editing ? 'Update' : 'Create' }}</button>
      <button v-if="editing" type="button" @click="resetForm">Cancel</button>
    </form>

    <table class="table-auto w-full border border-gray-300 border-collapse">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Image</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
          <td>
            <img :src="product.image" alt="Product Image" width="60" />
          </td>
          <td>
            <button @click="editProduct(product)">Edit</button>
            <button @click="deleteProduct(product.id)">Delete</button>
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

const products = ref([])
const form = ref({ name: '', price: '', image: '' })
const editing = ref(false)
const editId = ref(null)

const fetchProducts = async () => {
  try {
    products.value = await api.get('/product')
  } catch (error) {
    console.error(error)
  }
}

onMounted(fetchProducts)

const handleSubmit = async () => {
  try {
    if (editing.value) {
      await api.put(`/product/${editId.value}`, {
        name: form.value.name,
        price: form.value.price,
        image: form.value.image
      })
    } else {
      await api.post('/product', form.value)
    }
    await fetchProducts()
    resetForm()
  } catch (error) {
    console.error(error)
  }
}

const deleteProduct = async (id) => {
  if (!confirm('Are you sure you want to delete this product?')) return
  try {
    await api.del(`/product/${id}`)
    await fetchProducts()
  } catch (error) {
    console.error(error)
  }
}

const editProduct = (product) => {
  form.value = {
    name: product.name,
    price: product.price,
    image: product.image
  }
  editing.value = true
  editId.value = product.id
}

const resetForm = () => {
  form.value = { name: '', price: '', image: '' }
  editing.value = false
  editId.value = null
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