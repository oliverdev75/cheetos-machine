<template>
  <div>
    <h2>Users</h2>

    <!-- Formulario para crear/editar -->
    <form @submit.prevent="handleSubmit">
        <input v-model="form.name" placeholder="Name" required />
        <input v-model="form.email" placeholder="Email" required />
        <input v-if="!editing" v-model="form.password" type="password" placeholder="Password" required />
        <button type="submit">{{ editing ? 'Update' : 'Create' }}</button>
        <button v-if="editing" type="button" @click="resetForm">Cancel</button>
    </form>

    <table class="table-auto w-full border border-gray-300 border-collapse">
      <thead>
        <tr class="bg-gray-100">
          <th>Name</th>
          <th>Email</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-gray-100" v-for="user in users" :key="user.id">
          <td class="border border-gray-300 px-4 py-2">{{ user.name }}</td>
          <td class="border border-gray-300 px-4 py-2">{{ user.email }}</td>
          <td class="border border-gray-300 px-4 py-2">
            <button @click="editUser(user)">Edit</button>
            <button @click="deleteUser(user.id)">Delete</button>
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

const users = ref([])
const form = ref({ name: '', email: '', password: '' })
const editing = ref(false)
const editId = ref(null)

// Cargar usuarios
const fetchUsers = async () => {
  try {
    users.value = await api.get('/user')
  } catch (error) {
    console.error(error)
  }
}

onMounted(fetchUsers)

// Crear o actualizar usuario
const handleSubmit = async () => {
  try {
    if (editing.value) {
      await api.put(`/user/${editId.value}`, {
        name: form.value.name,
        email: form.value.email
        // No se envía password al editar
      })
    } else {
      await api.post('/user', form.value)
    }
    await fetchUsers()
    resetForm()
  } catch (error) {
    console.error(error)
  }
}

// Borrar usuario
const deleteUser = async (id) => {
  if (!confirm('Are you sure you want to delete this user?')) return
  try {
    await api.del(`/user/${id}`)
    await fetchUsers()
  } catch (error) {
    console.error(error)
  }
}

// Cargar datos para edición
const editUser = (user) => {
  form.value = { name: user.name, email: user.email }
  editing.value = true
  editId.value = user.id
}

// Limpiar formulario
const resetForm = () => {
  form.value = { name: '', email: '', password: '' }
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