<script setup lang="ts">
import { computed, reactive, useSlots } from 'vue'
import MatIcon from './MatIcon.vue'
import { type IconPosition } from '../types/button'

const slots = useSlots()

const {
    label,
    icon,
    iconPos,
    iconClass,
    white,
    fluid,
    text
} = withDefaults(
    defineProps<{
        label?: string,
        icon?: string,
        iconPos?: IconPosition,
        iconClass?: string,
        white?: boolean,
        fluid?: boolean,
        text?: boolean,
    }>(),
    { iconPos: 'left' }
)

const primary = computed(() => !white && !text)
const secondary = computed(() => (slots.default || label) && white && !text)

const renderedClass = reactive({
    'text-white bg-gazpacho hover:bg-btn-hover': primary,
    'bg-white text-gazpacho': secondary,
    'w-fit': computed(() => !fluid),
    'px-5': computed(() => fluid && !text && !icon && !slots.default && !label),
    'w-full justify-center': computed(() => fluid),
    'py-1 px-2': computed(() => icon && !text && !slots.default && !label),
    'px-5 py-1.5': computed(() => !icon && !text && (slots.default || label)),
})

</script>

<template>
    <button
        class="flex items-center gap-3 rounded-md hover:cursor-pointer"
        :class="renderedClass"
        v-bind="$attrs"
    >
        <mat-icon v-if="icon && iconPos == 'left'" :icon="icon" :class="iconClass" />
        <slot />
        {{ label }}
        <span v-if="!label && !slots.default && !icon">Button</span>
        <mat-icon v-if="icon && iconPos == 'right'" :icon="icon" :class="iconClass" />
    </button>
</template>