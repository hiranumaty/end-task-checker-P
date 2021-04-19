<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <v-main>
            <v-container fluid>
                <v-row>
                    <v-col>
                        <v-card>
                        <v-card-title>部署マスター</v-card-title>
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
                                        <th><v-btn :value="Dept['id']" @click="ModifyDept" >変更</v-btn></th>
                                    </tr>
                                </template>
                            </table>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card>
                            <v-card-title>タスクマスター</v-card-title>
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
                                        <th><v-btn :value="Task['id']" @click="ModifyTask">変更</v-btn></th>
                                    </tr>
                                </template>
                            </table>
                        </v-card>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="1">
                        <v-btn @click="CreateDept" class="CtrlBtn">新規部署作成</v-btn>
                    </v-col>
                    <v-col cols="1">
                        <v-btn @click="CreateTask" class="CtrlBtn">新規タスク作成</v-btn>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-btn id="ToMain" @click="goMain" class="CtrlBtn">メインページへ</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
import './stylesheet/ListStyle.css'
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
        ModifyDept(event){
            let id = event.currentTarget.value;
            this.$router.replace({path:'/DeptDetail/'+id})
        },
        ModifyTask(event){
            let id = event.currentTarget.value;
            this.$router.replace({path:'/TaskDetail/'+id})
        },
        CreateTask(){
            this.$router.replace({path:'/CreateTask/'})
        },
        CreateDept(){
            this.$router.replace({path:'/CreateDept/'})
        }
    },
}
</script>