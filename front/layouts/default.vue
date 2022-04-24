<template>
    <div class="layout">
        <HeaderComponent />
        <slot />
        <FooterComponent />
    </div>
</template>

<script setup>

</script>

<style lang="scss">
    .layout {
        background: rgba(0, 0, 0, 0.038);
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
</style>