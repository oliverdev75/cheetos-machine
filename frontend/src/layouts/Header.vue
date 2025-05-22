<script setup lang="ts">

</script>

<template>
  <div class="bg-[#E57600] w-full h-20 py-5 px-2 flex justify-center">
    <div class="w-[90%] flex items-center justify-between mx-15">
        <div>
          <router-link to=""><img src="./../../public/images/logo.svg" alt="" class="w-75 fixed"></router-link>
        </div>
        <nav class="text-white flex justify-between w-200 text-2xl font-bold">
          <router-link to="/">Home</router-link>
          <router-link to="/dashboard">Pedir</router-link>
          <router-link to="/about-us">Sobre nosotros</router-link>
          <router-link to="/account">Cuenta</router-link>
        </nav>
        <div class="flex items-center text-2xl font-bold text-white">
          <p>12 Tokens</p>
          <img src="./../../public/images/Frame.svg" alt="" class="w-15">
        </div>
    </div>
  </div>
</template>