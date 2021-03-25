<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <div>
            <table id="DeptData" class="DataTable">
                <tr class="header">
                    <th>部署ID</th>
                    <th>部署名</th>
                    <th>有効/無効</th>
                    <th>有効開始日</th>
                </tr>
                <template v-for="Dept in DeptData">
                    <tr :key="Dept.index">
                        <td><input type="text" v-bind:value="Dept['id']" readonly></td>
                        <td><input type="text" v-bind:value="Dept['deploy_name']"></td>
                        <td><input type="text" v-bind:value="Dept['valid_text']"></td>
                        <td><input type="text" v-bind:value="Dept['valid_start']"></td>
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
            DeptData:[],
        }
    },
    async created(){
        let AdminListAPI = new AdminListApi()
        let id = this.$route.params['target']
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.DeptData = AdminListAPI.getDeptDetail(this,id)
        console.log(this.DeptData)
    },
}
</script>