<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <h1>ログイン成功</h1>
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