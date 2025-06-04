<script setup lang="ts">
import { ref } from "vue"
import Api from "../utils/Api"
import Button from "../components/Button.vue"
import InputText from "../components/InputText.vue"
import { useRouter } from "vue-router"

const router = useRouter()
const api = Api.access()

const name = ref("")
const email = ref("")
const password = ref("")

const register = () => {
  api.post("/users", {
    name: name.value,
    email: email.value,
    password: password.value
  })
    .then(() => {
      router.push({ name: "login" })
    })
    .catch((error: any) => {
      console.error("Registration failed:", error)
    })
}

</script>

<template>
  <div class="flex-1 flex justify-center items-center">
    <div class="bg-gazpacho px-10 py-15 rounded-2xl flex flex-col gap-10">
      <h1 class="text-center text-white text-4xl">Register</h1>
      <div class="flex flex-col gap-6">
        <form @submit.prevent="register" class="flex flex-col gap-10 text-white">
          <div class="flex flex-col gap-4">
            <div class="flex gap-2 items-center">
                <label for="name">Name:</label>
                <InputText v-model="name" type="text" id="name" />
            </div>
            <div class="flex gap-2 items-center">
                <label for="email">Email:</label>
                <InputText v-model="email" type="email" id="email" />
            </div>
            <div class="flex gap-2 items-center">
              <label for="password">Password:</label>
                <InputText v-model="password" type="password" id="password" />
            </div>
          </div>
  
          <Button type="submit" white fluid>Register</Button>
        </form>
        <span class="text-white flex justify-center gap-2">
          Already have an account?
          <router-link :to="{ name: 'login' }" class="text-white text-center">
            <a class="text-[#052F5F] hover:text-blue-700">
              Log in here
            </a>
          </router-link>
        </span>
      </div>
    </div>
  </div>
</template>
