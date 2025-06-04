<script setup lang="ts">
import { ref, onMounted } from 'vue'
import useAuthStore from '../store/auth'
import MatIcon from '../components/MatIcon.vue'
import Button from '../components/Button.vue'
import { useRouter } from 'vue-router'
import useAuth from '../composables/auth'

const router = useRouter()
const authStore = useAuthStore()
const menuVisible = ref(false)
const { logout } = useAuth()

const navigate = (to: string | object) => {
  menuVisible.value = false
  router.push(to)
}

const pages = [
  { name: 'Home', path: '/' },
  { name: 'Carta', path: '/carta' },
  { name: 'About', path: '/nosotros' },
]

const logoutV = () => {
  menuVisible.value = false
  logout()
}

</script>

<template>
  <div class="navmenu-overlay"></div>
  <div class="bg-[#E57600] w-full py-5 px-2 flex justify-center">
    <div class="w-[90%] flex items-center justify-between">
        <div>
          <router-link to="/">
            <img src="/images/short_logo.png" alt="Gazpacho little logo" class="block lg:hidden w-12">
            <img src="/images/logo.svg" alt="Gazpacho big logo" class="hidden lg:block w-35">
          </router-link>
        </div>
        <Button class="static lg:hidden" icon="menu" text icon-class="text-white !text-3xl" @click="menuVisible = !menuVisible" />
        <div class="hidden lg:flex w-full justify-end items-center gap-4">
          <nav class="text-white flex gap-5 text-2xl font-bold">
            <router-link :to="{ name: 'home' }" class="hover:underline text-2xl">Home</router-link>
            <router-link :to="{ name: 'menu' }" class="hover:underline text-2xl">Pedir</router-link>
            <router-link :to="{ name: 'about' }" class="hover:underline text-2xl">Sobre nosotros</router-link>
            <template v-if="authStore.token">
              <div class="flex gap-1 items-center">
                <span>{{ authStore.user?.tokens }}</span>
                <img class="w-10" src="/images/token.png" alt="Tokens symbol">
              </div>
              <router-link :to="{ name: 'account' }" class="flex items-center gap-2">
                <mat-icon class="!text-3xl">account_circle</mat-icon>
                <span>Account</span>
              </router-link>
              <Button icon="logout" white class="px-5 text-red-500" @click="logout">Log out</Button>
            </template>
            <template v-else>
              <router-link :to="{ name: 'login' }" class="hover:underline text-2xl text-white">
                Login
              </router-link>
              <router-link :to="{ name: 'register' }" class="hover:underline text-2xl text-white">
                Register
              </router-link>
            </template>
          </nav>
        </div>
        <div class="
          flex lg:hidden absolute top-0 right-[-250px]
          h-screen w-[250px] px-10 py-5 flex-col gap-3
          bg-white text-gazpacho shadow-2xl transition-all duration-300 ease-in-out z-50"
          :class="{ 'menu-visible': menuVisible }"
        >
          <Button icon="close" text icon-class="text-gazpacho !text-3xl" @click="menuVisible = false" />
          <nav class="h-full flex flex-col justify-between text-2xl">
            <div class="flex flex-col gap-5 text-2xl">
              <a v-for="page in pages" :key="page.name" @click="navigate(page.path)" class="cursor-pointer hover:underline">
                {{ page.name }}
              </a>
            </div>
            <div class="flex flex-col gap-5 text-2xl items-center">
              <template v-if="authStore.token">
                <div class="flex gap-1 items-center">
                  <span>{{ authStore.user?.tokens }}</span>
                  <img class="w-10" src="/images/token_orange.png" alt="Tokens symbol">
                </div>
                <a @click="navigate({ name: 'account' })" class="flex items-center">
                  <Button text icon="account_circle">Account</Button>
                </a>
                <Button icon="logout" white class="text-red-500" @click="logoutV">Log out</Button>
              </template>
              <template v-else>
                <a @click="navigate({ name: 'login' })" class="flex items-center hover:underline hover:cursor-pointer">
                  Login
                </a>
                <a @click="navigate({ name: 'register' })" class="flex items-center hover:underline hover:cursor-pointer">
                  Register
                </a>
              </template>
            </div>
          </nav>
        </div>
    </div>
  </div>
</template>

<style scoped>

.menu-visible {
  transform: translateX(-250px);
}

/* .navmenu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: -1;
  transition: all .3s ease-in-out;
} */

</style>