<script setup lang="ts">
import { ref } from "vue"
import useAuth from "../composables/auth"
import Button from "../components/Button.vue"
import InputText from "../components/InputText.vue"

const auth = useAuth()

const email = ref("")
const password = ref("")

const login = async () => {
  await auth.login(email.value, password.value)
}

</script>

<template>
  <div class="flex-1 flex justify-center items-center bg-gazpacho">
    <div class="bg-white px-10 py-15 rounded-2xl flex flex-col gap-10">
      <h1 class="text-center text-gazpacho text-4xl">Log in</h1>
      <div class="flex flex-col gap-6">
        <form @submit.prevent="login" class="flex flex-col gap-10 text-gazpacho">
          <div class="flex flex-col gap-4">
            <div class="flex gap-2 items-center">
                <label for="email">Email:</label>
                <InputText v-model="email" type="email" id="email" />
            </div>
            <div class="flex gap-2 items-center">
              <label for="password">Password:</label>
                <InputText v-model="password" type="password" id="password" />
            </div>
          </div>
  
          <Button type="submit" fluid>Log in</Button>
        </form>
        <span class="text-black flex justify-center gap-2">
          Don't have an account?
          <router-link :to="{ name: 'register' }" class="text-black text-center">
            <a class="text-blue-500 hover:text-blue-700">
              Register here
            </a>
          </router-link>
        </span>
      </div>
    </div>
  </div>
</template>
