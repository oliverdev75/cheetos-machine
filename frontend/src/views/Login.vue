<script setup lang="ts">
import { ref } from "vue";
import useLogin from "../composables/useAuth";

const { getUser, tryToLogin } = useLogin();

const email = ref("");
const password = ref("");
const user = ref(); // Aquí guardaremos al usuario una vez logueado

async function login() {
    console.log("Login");
    console.log(email.value);

    await tryToLogin(email.value, password.value);

    // Una vez logueado, obtenemos el usuario desde el token
    user.value = getUser();
    console.log("Usuario logueado:", user.value);
}
</script>

<template>
    <h1>Login</h1>
    <form @submit.prevent="login" class="d-flex">
        <div>
            <label for="email">Email:</label>
            <input v-model="email" type="email" id="email" />
        </div>

    <div>
      <label for="password">Password:</label>
      <input v-model="password" type="password" id="password" />
    </div>

    <input type="submit" value="Login" />
  </form>

  <div v-if="user">
    <h2>Bienvenido, {{ user.name || user.email || 'Usuario' }}</h2>
    <p>ID: {{ user.user_id }}</p>
    <p>Email: {{ user.email }}</p>
  </div>
</template>
