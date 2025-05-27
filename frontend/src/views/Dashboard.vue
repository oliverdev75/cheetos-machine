<script setup lang="ts">
import { onMounted } from 'vue';
import useApi from '../composables/api';
import useAuth from '../composables/auth';

const api = useApi();


const tryLogin = async () => 
{
  const tryToLogin = useAuth();
  const response = await tryToLogin("test@demo.com");
  console.log(response);
};

/* TEST (se puede borrar si es necesario) */
const ping = async () => 
{
  try {
    const response = await api.get('/api/ping');
    console.log(response.data);
  } catch (error) {
    console.error('Error ping:', error);
  }
}
</script>

<template>
  <div class="background">
    <div class="mainDashboardGrid">

      <div class="grid-item" style=" grid-area: 1 / 2 / 2 / 3; background: #9EECA0;">
        <Button @click="tryLogin">
          Login!
        </Button>
        <Button @click="ping">
          Ping!
        </Button>
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