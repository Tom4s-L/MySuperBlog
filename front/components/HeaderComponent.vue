<template>
    <div class="header">
        <NuxtLink to="/">
            <h1 class="title">
                <img src="@/assets/images/blog.png" 
                    alt="Logo du site" 
                    class="title__logo"
                >
                Mon super Blog
            </h1>
        </NuxtLink>
        <NavbarComponent />
    </div>
</template>

<script setup>
    
</script>

<style lang="scss" scoped>
    .header {
        height: 10vh;
        background: rgba(0, 0, 0, 0.299);
        color: white;

        display: flex;
        align-items: center;
        justify-content: space-around;
    }

    .title {
        font-size: 1.5rem;

        &__logo {
            max-height: 2rem;
        }
    }
</style>