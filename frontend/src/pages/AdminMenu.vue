<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <h1>管理者画面</h1>
        <div>
            <h3>部署マスター</h3>
            <table id="DeptArea" class="DataTable">
                <tr class="header">
                    <th>部署ID</th>
                    <th>部署名</th>
                    <th>有効/無効</th>
                    <th>有効開始日</th>
                    <th></th>
                </tr>
            </table>
        </div>
        <div>
            <h3>タスクマスター</h3>
            <table id="TaskArea" class="DataTable">
                <tr class="header">
                    <th>タスクID</th>
                    <th>タスク名</th>
                    <th>有効/無効</th>
                    <th>有効開始日</th>
                    <th></th>
                </tr>
            </table>
        </div>
        <button id="ToMain" @click="goMain">メインページへ</button>
    </v-app>
</template>
<script>
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import AdminListApi from "@/services/AdminListApi";
export default{
    components:{
        GlobalHeader,
        GlobalMessage,
    },
    data(){
        return{
            DeptList:[],
            taskList:[],
        }
    },
    async created(){
        let AdminListApi = new AdminListApi();
        this.DeptList = AdminListApi.GetDeptsMaster(this);
        this.taskList = AdminListApi.getTaskMaster(this);
    },
    methods:{
        goMain(){
            this.$router.replace({path:'/MainPage'})
        },
    },
    }
</script>