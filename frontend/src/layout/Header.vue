<script setup lang="ts">

</script>

<template>
  <div class="bg-[#E57600] w-full h-20 py-5 px-2 flex justify-center">
    <div class="w-[90%] flex items-center justify-between mx-15">
        <div>
          <RouterLink to=""><img src="./../../public/images/logo.svg" alt="" class="w-75 fixed"></RouterLink>
        </div>
        <nav class="text-white flex justify-between w-200 text-2xl font-bold">
          <RouterLink :to="{ name: 'home' }">Home</RouterLink>
          <RouterLink :to="{ name: 'menu' }">Pedir</RouterLink>
          <RouterLink :to="{ name: 'about' }">Sobre nosotros</RouterLink>
          <RouterLink :to="{ name: 'account' }">Cuenta</RouterLink>
        </nav>
        <div class="flex items-center text-2xl font-bold text-white">
          <p>12 Tokens</p>
          <img src="./../../public/images/Frame.svg" alt="" class="w-15">
        </div>
    </div>
  </div>
</template>
