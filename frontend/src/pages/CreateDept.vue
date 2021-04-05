<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <h1>新規部署作成</h1>
        <table class="DataTable">
            <tr class="header">
                <th>部署ID</th>
                <th>部署名</th>
                <th>有効開始日</th>
                <th></th>
            </tr>
            <tr>
                <td><input type="text" id="input_id"></td>
                <td><input type="text" id="input_name"></td>
                <td><input type="text" id="input_start" min="1900-01-01"></td>
                <td><button @click="ExCreate">追加</button></td>
            </tr>
        </table>
        <button @click="goAdmin">管理画面へ</button>
    </v-app>
</template>

<script>
import './stylesheet/ListStyle.css'
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import api from '@/services/api'
export default{
    components:{
        GlobalHeader,
        GlobalMessage
    },
    created(){
        this.host = process.env.VUE_APP_API_BASE_URL;
    },
    methods:{
        ExCreate(){
            let input_id = document.getElementById("input_id").value;
            let input_name = document.getElementById("input_name").value;
            let input_start = document.getElementById("input_start").value;
            let nowdate = new Date()
            let newdata={
                id:input_id,
                deploy_name:input_name,
                valid_flg:false,
                valid_start:input_start,
                created_at:this.FormatDate(nowdate)
            }
            api.post(this.host+"/MasterControll/getDepts/create/",newdata)
            .then(()=>{
               this.$router.replace({path:'/AdminMenu'}) 
            });
        },
        FormatDate(Date){
            let year  = '' + Date.getFullYear();
            let month = '' + (Date.getMonth() + 1);
            let day = '' + Date.getDate()
            if(month.length < 2)
                month = '0' + month
            if(day.length < 2)
                day = '0' + day
            return [year,month,day].join('-')
        },
        goAdmin(){
            this.$router.replace({path:'/AdminMenu/'})
        }
    },
}
</script>