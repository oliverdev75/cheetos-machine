<script setup>
import { ref } from 'vue'
import Users from "./Users.vue"
import Orders from "./Orders.vue"
import Products from "./Products.vue"
import Roles from "./Roles.vue"

let pageSelector = ref(1)

</script>

<template>
<h1>Admin Panel</h1>
<hr>
<button @click="pageSelector = 1">Users</button>
<button @click="pageSelector = 2">Roles</button>
<button @click="pageSelector = 3">Products</button>
<button @click="pageSelector = 4">Orders</button>
<hr/>

<Users v-if="pageSelector == 1" />
<Roles v-if="pageSelector == 2" />
<Products v-if="pageSelector == 3" />
<Orders v-if="pageSelector == 4" />

</template>