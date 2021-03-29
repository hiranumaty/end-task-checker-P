<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <div>
            <table id="TaskData" class="DataTable">
                <tr class="header">
                    <th>タスクID</th>
                    <th>タスク名</th>
                    <th>有効/無効</th>
                    <th>有効開始日</th>
                    <th></th>
                </tr>
                <template v-for="Task in TaskData">
                    <tr :key="Task.index">
                        <td><input type="text" id="input_id" v-bind:value="Task['id']" readonly></td>
                        <td><input type="text" id="input_name" v-bind:value="Task['Task_name']"></td>
                        <td><input type="button" id="input_flg" v-bind:value="Task['valid_text']" @click="changeValid_Text"></td>
                        <td><input type="text" id="input_start" v-bind:value="Task['valid_start']"></td>
                        <td><button @click="changeEvent">変更</button></td>
                    </tr>
                </template>
            </table>
        </div>
        <button @click="goAdmin">管理画面へ</button>
    </v-app>
</template>
        
<script>
import './stylesheet/ListStyle.css'
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import AdminListApi from "@/services/AdminListApi";
import api from '@/services/api'
export default{
    components:{
        GlobalHeader,
        GlobalMessage,
    },
    data(){
        return{
            TaskData:[],
        }
    },
    async created(){
        let AdminListAPI = new AdminListApi()
        let id = this.$route.params['target']
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.TaskData = AdminListAPI.getTaskDetail(this,id)
    },
    methods:{
        changeValid_Text(event){
            let text = event.target.value
            text = (text=='有効') ?'無効':'有効';
            event.target.value = text
        },
        changeEvent(){
            let update_id = document.getElementById("input_id").value;
            let update_Task_name = document.getElementById("input_name").value;
            let update_valid_flg = document.getElementById("input_flg").value;
            let update_valid_start = document.getElementById("input_start").value;
            let flg = (update_valid_flg=='有効')? true:false;

            let update_data = {
                Task_name:update_Task_name,
                valid_flg:flg,
                valid_start:update_valid_start,
            }

            api.patch(this.host+"/MasterControll/getTasks/"+update_id+"/update/",update_data)
            .then(()=>{
                this.$router.replace({path:'/AdminMenu/'})
            });
        },
        goAdmin(){
            this.$router.replace({path:'/AdminMenu/'})
        }
    }
}
</script>