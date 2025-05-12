<script setup lang="ts">

</script>

<template>
    <div class="mainDashboardGrid">
        <div class="grid-item" style=" grid-area: 1 / 2 / 2 / 3;"> </div>
        <div class="grid-item" style=" grid-area: 2 / 2 / 6 / 3;"> </div>
        <div class="grid-item" style=" grid-area: 1 / 1 / 4 / 2;"> </div>
        <div class="grid-item" style=" grid-area: 4 / 1 / 6 / 2;"> </div>
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

    width: 85%;
    height: 85vh;
    margin: auto;
}

.grid-item
{
    width: 100%;
    height: 100%;
    border-radius: 1rem;
    background-color: aqua;
}
</style>