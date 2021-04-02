<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <h1>新規タスク作成</h1>
        <table class="DataTable">
            <tr class="header">
                <th>タスクID</th>
                <th>タスク名</th>
                <th>有効開始日</th>
                <th></th>
            </tr>
            <tr>
                <td><input type="text" id="input_id"></td>
                <td><input type="text" id="input_name"></td>
                <td><input type="text" id="input_start" ></td>
                <td><button @click="ExCreate">追加</button></td>
            </tr>
        </table>
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
            console.log(input_id)
            console.log(input_name)
            console.log(input_start)
            console.log(nowdate.toLocaleDateString())
            let newdata={
                id:input_id,
                Task_name:input_name,
                valid_flg:false,
                valid_start:input_start,
                created_at:nowdate.toLocaleDateString()
            }
            api.post(this.host+"/MasterControll/getTasks/create/",newdata)
            .then(()=>{
               this.$router.replace({path:'/AdminMenu'}) 
            });
        }
    },
}
</script>