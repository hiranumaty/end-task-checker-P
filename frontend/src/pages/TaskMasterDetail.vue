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
                </tr>
                <template v-for="Task in TaskData">
                    <tr :key="Task.index">
                        <td><input type="text" v-bind:value="Task['id']" readonly></td>
                        <td><input type="text" v-bind:value="Task['Task_name']"></td>
                        <td><input type="text" v-bind:value="Task['valid_text']"></td>
                        <td><input type="text" v-bind:value="Task['valid_start']"></td>
                    </tr>
                </template>
            </table>
        </div>
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
            TaskData:[],
        }
    },
    async created(){
        let AdminListAPI = new AdminListApi()
        let id = this.$route.params['target']
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.TaskData = AdminListAPI.getTaskDetail(this,id)
    },
}
</script>