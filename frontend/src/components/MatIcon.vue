<script setup lang="ts">
import { useSlots } from 'vue'


const slots = useSlots()

defineProps<{
    icon?: string
}>()

</script>

<template>
    <i class="material-symbols-rounded" v-bind="$attrs">
        <span v-if="!icon && !slots.default">radio_button_unchecked</span>
        {{ icon || '' }}
        <slot />
    </i>
</template>