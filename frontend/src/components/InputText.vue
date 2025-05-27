<script setup lang="ts">

const value = defineModel()

</script>

<template>
    <input type="text" v-model="value" v-bind="$attrs" class="border-2 border-neutral-200 px-3 py-1 rounded-md bg-white text-black" />
</template>