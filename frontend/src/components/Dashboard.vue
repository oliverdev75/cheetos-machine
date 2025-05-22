<script setup lang="ts">

</script>

<template>
<p>Dashboard</p>
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
}

.grid-item
{
    width: 255px;
    height: 64px;
    background-color: aqua;
}
</style>