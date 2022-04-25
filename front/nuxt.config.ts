import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    app: {
        head: {
            link: [
                { 
                    rel: "stylesheet",
                    href: "https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Poppins:wght@800;900&display=swap",
                }
            ]
        }
    },

    css: [
        "@/node_modules/destyle.css/destyle.min.css",
        "@/assets/styles/main.scss"
    ],

    buildModules: [
        "@nuxtclub/slugify"
    ],

    slugify: {
        extend: {
            '_': '-',
            '&': '-',
        }
    }
})
