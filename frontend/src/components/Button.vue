<script setup lang="ts">
import { onMounted, useSlots } from 'vue'
import MatIcon from './MatIcon.vue'
import { type IconPosition } from '../types/button'

const slots = useSlots()

withDefaults(
    defineProps<{
        label?: string,
        icon?: string,
        iconPos?: IconPosition,
        white?: boolean
    }>(),
    { iconPos: 'left' }
)

</script>

<template>
    <button class="flex items-center gap-3 text-white bg-gazpacho px-5 py-2 rounded-lg hover:cursor-pointer hover:bg-amber-500 m-4" v-bind="$attrs">
        <MatIcon v-if="icon && iconPos == 'left'" :icon="icon" />
        <slot />
        {{ label }}
        <span v-if="!label && !slots.default">Button</span>
        <MatIcon v-if="icon && iconPos == 'right'" :icon="icon" />
    </button>
</template>