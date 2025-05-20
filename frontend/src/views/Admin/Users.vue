<template>
<h2>Users</h2>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="user in users">
            
        </tr>
    </tbody>
</table>


</template>

<script setup>
import useApi from "../../composables/api"
import { ref, onMounted } from "vue"

const api = useApi()

const users = ref([])

onMounted(async () => {
    users.value = await api.get("users")
})


</script>