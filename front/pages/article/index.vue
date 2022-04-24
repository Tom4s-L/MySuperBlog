<template>
    <main class="main">
        <h2 class="page-title">
            Ecrire un article
        </h2>

        <form action="" class="form">
            <label for="form-title" class="form__label">Titre de l'article</label>
            <input type="text" id="form-title" name="form-title" class="form__control form__control--title">

            <label for="form-content" class="form__label">Contenu de l'article</label>
            <textarea id="form-content" name="form-content" cols="30" rows="10" class="form__control form__control--content"></textarea>

            <button type="submit" class="form__button">
                Envoyer
            </button>
        </form>
    </main >
</template>

<script setup>

</script>

<style lang="scss" scoped>    
    .main {
        justify-content: center;
    }
   
   .form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: clamp(300px, 30vw, 600px);

        &__label {
            margin: 1rem 0 0.2rem 0;
        }

        &__control {
            background: white;
        }

        &__control--content {
            resize: vertical;
        }

        &__button {
            background: rgb(3, 198, 3);
            max-width: 30%;
            text-align: center;
            padding: 1rem;
            margin: 1rem auto;
            color: white;
            font-weight: bold;
        }
   }
</style>