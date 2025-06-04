<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Button from './Button.vue'
import Api from '../utils/Api'
import { API_URL } from '../constants/api';

const props = defineProps<{
    id?: number,
    name?: string,
    tokens?: number,
    image?: string,
}>()

</script>

<template>
    <article class="flex flex-col">
        <img
          :src="API_URL + `/products/image/${id}`"
          alt="Image of the product"
          class="m-auto h-60 object-cover"
        />
        <div class="w-full flex flex-col gap-3 items-center">
          <strong class="text-white text-center text-4xl text-shadow-lg">{{ name }}</strong>
          <router-link :to="{ name: 'buy-product', params: { id: id } }">
            <Button
              icon="shopping_cart"
              white
              class="px-5 py-3 text-3xl gap-7"
              icon-class="!text-4xl"
            >
              {{  tokens }} Tokens
            </Button>
          </router-link>
        </div>
      </article>
</template>