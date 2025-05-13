<script setup lang="ts">

</script>

<template>

    <header>
        <img class="logo" src="./Cheetos_logo.png">
        <nav>
            <router-link class="route-link" to="/">Inicio</router-link>
            <router-link class="route-link" to="/dashboard">Dashboard</router-link>
        </nav>
    </header>

</template>

<style scoped>
header {
    padding: 16px;
    width: 100%;
    background-color: #E57600;

    display: flex;
    flex-direction: row;

    box-sizing: border-box;
}

nav {
    margin-left: 32px;
    margin-right: 32px;
    align-content: space-between;

    display: flex;

    gap: 32px;
    font-size: larger;
}

.route-link {
    color: white;
    text-decoration: none;
}

.logo {
    width: 25vw;
    height: auto;
}
</style>