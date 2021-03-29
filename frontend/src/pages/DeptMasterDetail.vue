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
                    <th></th>
                </tr>
                <template v-for="Dept in DeptData">
                    <tr :key="Dept.index">
                        <td><input type="text" id="input_id" v-bind:value="Dept['id']" readonly></td>
                        <td><input type="text" id="input_name" v-bind:value="Dept['deploy_name']"></td>
                        <td><input type="button" id="input_flg" v-bind:value="Dept['valid_text']" @click="changeValid_Text"></td>
                        <td><input type="text" id="input_start" v-bind:value="Dept['valid_start']"></td>
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
            DeptData:[],
        }
    },
    async created(){
        let AdminListAPI = new AdminListApi()
        let id = this.$route.params['target']
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.DeptData = AdminListAPI.getDeptDetail(this,id)
    },
    methods:{
        changeValid_Text(){
            let text = event.target.value
            text = (text=='有効') ?'無効':'有効';
            event.target.value = text
        },
        changeEvent(){
            let update_id = document.getElementById("input_id").value;
            let update_deploy_name = document.getElementById("input_name").value;
            let update_valid_flg = document.getElementById("input_flg").value;
            let update_valid_start = document.getElementById("input_start").value;
            let flg = (update_valid_flg=='有効')? true:false;

            let update_data ={
                deploy_name:update_deploy_name,
                valid_flg:flg,
                valid_start:update_valid_start,
            }

            api.patch(this.host+"/MasterControll/getDepts/"+update_id+"/update/",update_data)
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