<script setup lang="ts">
import { ref, onMounted } from 'vue'
import useAuthStore from '../store/auth'
import MatIcon from '../components/MatIcon.vue';

const authStore = useAuthStore()
</script>

<template>
  <div class="bg-[#E57600] w-full h-20 py-5 px-2 flex justify-center">
    <div class="w-[90%] flex items-center justify-between mx-15">
        <div>
          <router-link to=""><img src="./../../public/images/logo.svg" alt="" class="w-75 fixed"></router-link>
        </div>
        <nav class="text-white flex gap-5 text-2xl font-bold">
          <router-link :to="{ name: 'home' }">Home</router-link>
          <router-link :to="{ name: 'menu' }">Pedir</router-link>
          <router-link :to="{ name: 'about' }">Sobre nosotros</router-link>
        </nav>
        <div v-if="authStore.user" class="flex items-center text-2xl font-bold text-white">
          <p>{{ authStore.user.cash }} €</p>
          <router-link :to="{ name: 'account' }">
            <MatIcon icon="account_circle" class="ml-4 mr-2 text-3xl" />
            <span>Account</span>
          </router-link>
        </div>
        <div v-else class="flex gap-3">
          <router-link :to="{ name: 'login' }">
            <div class="flex items-center text-2xl text-white">
              <span class="ml-2 hover:underline">Login</span>
            </div>
          </router-link>
          <router-link :to="{ name: 'register' }">
            <div class="flex items-center text-2xl text-white">
              <span class="ml-2 hover:underline">Register</span>
            </div>
          </router-link>
        </div>
    </div>
  </div>
</template>
