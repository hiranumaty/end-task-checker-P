<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <h1><router-link :to="{name:'MainPage'}">メインページへ</router-link></h1>
    </v-app>
</template>
<script>
    //import api from '@/services/api'
    import GlobalHeader from "@/components/GlobalHeader.vue";
    import GlobalMessage from "@/components/GlobalMessage.vue";
    export default {
        components: {
        GlobalHeader,
        GlobalMessage
        },
        
    }
</script>