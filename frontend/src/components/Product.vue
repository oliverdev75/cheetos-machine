<script setup lang="ts">
import Button from './Button.vue'

defineProps<{
    id?: number,
    name?: string,
    price?: number,
    image?: string,
    buyCallback: (id: number) => void
}>()

</script>

<template>
    <article class="flex flex-col">
        <img
            :src="image"
            alt="Imagen del product"
            class="m-auto h-60 object-cover"
        />
        <div class="w-full flex flex-col gap-3 items-center">
          <strong class="text-white text-center text-4xl text-shadow-lg">{{ name }}</strong>
          <Button
            icon="shopping_cart"
            white
            class="px-5 py-3 text-3xl gap-7"
            icon-class="!text-4xl"
            @click="buyCallback(id)"
          >
            {{  price.toFixed(2).replace('.', ',') }}€
          </Button>
        </div>
      </article>
</template>