<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <div id="DeptArea">
            <ul>
                <li>部署マスター管理
                    <ul>
                        <li>部署名変更</li>
                        <li>部署追加</li>
                        <li>有効/無効切り替え</li>
                    </ul>
                </li>
            </ul>
        </div>
        <div id="TaskArea">
            <ul>
                <li>タスクマスター管理
                    <ul>
                        <li>タスク名変更</li>
                        <li>タスク追加</li>
                        <li>有効/無効切り替え</li>
                    </ul>
                </li>
            </ul>
        </div>
        <button id="ToMain" @click="goMain">メインページへ</button>
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
        methods:{
            goMain(){
                this.$router.replace({path:'/MainPage'})
            }
        }
    }
</script>