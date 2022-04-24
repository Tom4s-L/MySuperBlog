<template>
    <main class="main">
        <h2 class="page-title">
            Des articles qu'ils sont trop bien pour les lire ! 
        </h2>

        <div class="articles">
            <ArticleComponent 
                v-for="article in data" 
                :key="article.title" 
                :title="article.title"
                :creationDate="article.creationDate"
                :content="article.content"
            />
        </div>
        
    </main>
</template>

<script setup>
    let data = [
        {
            title: "Le premier article qui déchire",
            creationDate: "2021-12-04",
            content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque sint delectus possimus aspernatur nulla. Cumque quasi corrupti iusto illo ratione, eligendi nisi suscipit sit voluptatem et, dolores pariatur sequi? Vitae sunt dignissimos voluptate accusantium?"
        },
        {
            title: "Un oiseau sans ailes, bin ca ne vole pas !",
            creationDate: "2022-01-22",
            content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque sint delectus possimus aspernatur nulla. Cumque quasi corrupti iusto illo ratione, eligendi nisi suscipit sit voluptatem et, dolores pariatur sequi? Vitae sunt dignissimos voluptate accusantium? Soluta, animi accusantium distinctio consequuntur fugiat vero dolorum a, error culpa ab nam asperiores doloribus repellat id blanditiis autem quisquam, dicta deserunt. Accusantium voluptatum asperiores vero dignissimos consectetur aliquam ratione eum, iusto culpa, natus excepturi ex? Consequatur exercitationem in sequi qui aspernatur a magnam. Deleniti, fugiat?"
        },
        {
            title: "Comment faire pour charger son portable dans la forêt ?",
            creationDate: "2022-01-22",
            content: "Bin il n'y a pas le choix en fait... il faut pédaler !! C'est le grand tout un jour qui a dit: ' S'il n'y a pas de jus quand tu branches dans le cochon, c'est que tu t'es trompé de sens !'"
        }
    ];
</script>

<style lang="scss" scoped>
    .articles {
        min-width: 300px;
        max-width: 50vw;
    }
</style>