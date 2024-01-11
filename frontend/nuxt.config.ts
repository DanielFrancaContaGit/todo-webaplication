import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  // ssr: false,
  css: [
    "~/assets/main.scss",
    'vuetify/lib/styles/main.sass',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  build: {
    transpile: ['vuetify'],
  },

  runtimeConfig: {
    public: {
      SERVER_URL: process.env.SERVER_URL,
      LOGIN_TOKEN: process.env.LOGIN_TOKEN,
    }
  }

})
