<script setup lang="ts">
import { onMounted } from 'vue';
import useApi from '../composables/api';

const api = useApi();

onMounted(async () => {
   
})

const login = async () => {
  try {
    const response = await api.post('/login', {
      "email" : 'test@demo.com'
    });
    console.log('Login exitoso:', response.data);
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
  }
};
</script>

<template>
    <div class="background">
        <div class="mainDashboardGrid">

            <div class="grid-item" style=" grid-area: 1 / 2 / 2 / 3; background: #9EECA0;"> 
                <button @click="login">
                    Login!
                </button>
            </div>

            <div class="grid-item" style=" grid-area: 2 / 2 / 6 / 3; background: #9D8DE0;"> </div>
            <div class="grid-item" style=" grid-area: 1 / 1 / 4 / 2; background: #9D8DE0;"> </div>
            <div class="grid-item" style=" grid-area: 4 / 1 / 6 / 2; background: #9EECA0;"> </div>
        </div>
    </div>
</template>

<style scoped>
.mainDashboardGrid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(5, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;

    gap: 3rem;

    margin: auto;
    margin-top: 16px;
    width: 90%;
    height: 90vh;
}

.grid-item {
    width: 100%;
    height: 100%;

    border-radius: 1rem;
    box-shadow: 0 0 8px rgb(240, 240, 240);
}
</style>