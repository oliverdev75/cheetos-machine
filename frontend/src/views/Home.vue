<script setup lang="ts">
import { ref } from 'vue'

const title = ref('Gazpacho machine')
</script>

<template>
    <div class="home-body w-full h-[90vh] flex justify-evenly items-center">
      <div class="flex justify-center items-center w-[50%] flex-col">
        <img src="./../../public/images/Home_Text.svg" class="w-[80%]">
        <router-link to="dashboard" class="px-100 py-10 bg-amber-600">Entrar</router-link>
      </div>
      <div>
        <img src="./../../public/images/Narangin_1.png" alt="" class="w-150">
      </div>
    </div>
</template>