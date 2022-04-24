<template>
    <article class="article">
        <section class="article__reactions">
            <span @click="increaseNblikes" class="article__reactions--likes">❤️{{ nbLikes }}</span>
            |
            <span @click="increaseNbunlikes" class="article__reactions--unlikes">💔{{ nbUnlikes }}</span>
        </section>
        <h3 class="article__title">
            {{ title }}
        </h3>
        <section class="article__infos">
            <span class="infos__creation-date">{{ creationDate }}</span>
            <span class="infos__author"> - Posté par: {{ author }}</span>
            <!-- <span class="infos__update--date">Mis à jour le: Date de mise à jour içi</span> -->
        </section>
        <section class="article__content">
            {{ content }}
        </section>
        <div class="article__button-wrapper">
            <NuxtLink 
                :to="'/article/' + slugifiedTitle"
                class="article__button"
            >
                Voir plus
            </NuxtLink>
        </div>
    </article>
</template>

<script setup>
    import slugify from 'slugify';
    
    const props = defineProps({
        title: {
            type: String,
            default: 'Le titre de l\'article '
        },
        author: {
            type: String,
            default: 'Anonymous'
        },
        creationDate: {
            type: String,
            default: function() { return new Date().toDateString()}
        },
        content: {
            type: String,
            default: 'De là le succès du petit paysan Julien. Elle trouva des jouissances douces, et toutes brillantes du charme de la nouveauté, dans la sympathie de cette âme noble et fière. Mme de Rênal lui eut bientôt pardonné son ignorance extrême qui était une grâce de plus, et la rudesse de ses façons qu’elle parvint à corriger.'
        }
    })

    const slugifiedTitle = slugify(props.title, { lower: true});
    
    let nbLikes = ref(0);
    let nbUnlikes = ref(0);
    const increaseNblikes = () => {
        nbLikes.value++;
    }
    const increaseNbunlikes = () => {
        nbUnlikes.value++;
    }
</script>

<style lang="scss" scoped>
    .article {
        border: 2px solid rgba(0, 0, 0, 0.298);
        border-radius: 8px;
        padding: 1rem 2rem 1rem 2rem;
        margin-bottom: 2rem;
       
       &__title {
            font-size: 1.5rem;
        }

        &__reactions {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 0.5rem;
        }

        &__reactions--likes {
            margin-right: 5px;
        }

        &__infos {
            margin-bottom: 2rem;
            color: rgba(0, 0, 254, 0.576);
        }

        &__content {
            margin-bottom: 2rem;
        }

        &__button-wrapper {
            display: flex;
            justify-content: flex-end;
        }

        &__button {
            border: 1px solid rgba(0, 0, 0, 0.301);
            border-radius: 3px;
            padding: 0.2rem 0.5rem 0.2rem 0.5rem;
        }
    }
</style>