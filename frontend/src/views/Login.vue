<script setup>
import { ref } from "vue";
import useLogin from "../composables/useAuth";

const email = ref("");
const password = ref(""); // si luego lo necesitas

const tryToLogin = useLogin();

async function Login() {
    console.log("Login");
    console.log(email.value);

    await tryToLogin(email.value, password.value);
}
</script>

<template>
    <h1>Login</h1>
    <form @submit.prevent="Login" class="d-flex">
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
</template>
