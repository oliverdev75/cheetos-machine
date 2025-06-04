<script setup lang="ts">
import Header from "./layout/Header.vue"
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import useAuthStore from './store/auth'
import Api from "./utils/Api"

const router = useRouter()
const authStore = useAuthStore()
const api = Api.access()

onMounted(() => {
  api.get('/user').then(data => {
    authStore.user = data.user
    router.push({ name: 'menu' })
  })
  
})

</script> 

<template>
  <Header />
  <router-view />
</template>
