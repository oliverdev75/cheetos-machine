<script setup lang="ts">
import { ref } from 'vue'

const message = ref('Welcome to the Home Page!')
</script>

<template>
    <h1>{{ message }}</h1>
</template>