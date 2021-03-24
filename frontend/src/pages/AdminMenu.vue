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
                <template v-for="Dept in DeptList">
                    <tr :key="Dept.index">
                        <th>{{Dept["id"]}}</th>
                        <th>{{Dept["deploy_name"]}}</th>
                        <th>{{Dept["valid_text"]}}</th>
                        <th>{{Dept["valid_start"]}}</th>
                        <th>変更</th>
                    </tr>
                </template>
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
                <template v-for="Task in taskList">
                    <tr :key="Task.index">
                        <th>{{Task["id"]}}</th>
                        <th>{{Task["Task_name"]}}</th>
                        <th>{{Task["valid_text"]}}</th>
                        <th>{{Task["valid_start"]}}</th>
                        <th>変更</th>
                    </tr>
                </template>
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
        let AdminListAPI = new AdminListApi();
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.DeptList = AdminListAPI.GetDeptsMaster(this);
        this.taskList = AdminListAPI.getTaskMaster(this);
    },
    methods:{
        goMain(){
            this.$router.replace({path:'/MainPage'})
        },
    },
    }
</script>