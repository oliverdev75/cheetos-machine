<script setup lang="ts">
import { useSlots } from 'vue'
import MatIcon from './MatIcon.vue'
import { type IconPosition } from '../types/button'

const slots = useSlots()

withDefaults(
    defineProps<{
        label?: string,
        icon?: string,
        iconPos?: IconPosition,
        iconClass?: string,
        white?: boolean,
        fluid?: boolean
    }>(),
    { iconPos: 'left' }
)

</script>

<template>
    <button
        class="flex items-center gap-3 px-2 py-2 rounded-md hover:cursor-pointer m-4"
        :class="{
            'text-white': !white,
            'bg-gazpacho': !white,
            'bg-btn-hover': !white,
            'bg-white': white,
            'text-gazpacho': white,
            'w-fit': !fluid,
            'w-full': fluid
        }"
        v-bind="$attrs"
    >
        <MatIcon v-if="icon && iconPos == 'left'" :icon="icon" :class="iconClass" />
        <slot />
        {{ label }}
        <span v-if="!label && !slots.default">Button</span>
        <MatIcon v-if="icon && iconPos == 'right'" :icon="icon" :class="iconClass" />
    </button>
</template>