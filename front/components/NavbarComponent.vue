<template>
    <nav class="navbar">
        <NuxtLink to="/article" class="link">
            <img src="@/assets/images/write.png" alt="Illustration de rédaction" class="link__img">
            Ecrrire un article
        </NuxtLink>
    </nav>
</template>

<script setup>

</script>

<style lang="scss" scoped>
    .link {
        display: flex;
        align-items: center;
        color: white;

        &__img {
            max-height: 1.2rem;
            margin-right: 0.5rem;
        }
    }
</style>