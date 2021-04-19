<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <v-main>
            <v-container fluid >
                <v-row name="SearchField">
                    <v-col cols="12">
                        <input  class="SearchMonthField" type="text" v-model="TargetMonth" maxlength="6">
                        <button @click="SearchMonth" class="SearchButton">検索</button>
                    </v-col> 
                </v-row>
                <v-row>
                    <v-col cols="12">
                        <table  class="DataTable">
                            <tr class="header">
                                <template v-for="Column in taskListColumns">
                                    <th :key="Column.index">{{Column.text}}</th>
                                </template>
                            </tr>
                        <template v-for="toDodata in toDoDatas">
                            <tr :key="toDodata.index">
                                <template v-for="cell in toDodata">
                                    <td :key="cell.index">
                                        {{cell.text}}
                                    </td>
                                </template>
                            </tr>
                        </template>
                        </table>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
import "./stylesheet/ListStyle.css"
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import ListStatusApi from "@/services/ListStatusApi"
import api from "@/services/api";
export default{
    components:{
        GlobalHeader,
        GlobalMessage,
    },
    data(){
        return{
            thisMonth:"",
            TargetMonth:"",
            taskLength:"",
            taskListColumns:[],
            DeptList:[],
            toDoDatas:[],
        }
    },
    watch:{
        async $route(){
            this.fetchData()
        }
    },
    async created(){
        this.fetchData()
    },
    methods:{
        async fetchData(){
            //データの取得の際に実行される
            //SearchMonthとMainPage上手くまとめられるか
            let ListStatusAPI = new ListStatusApi()
            let today = new Date();
            let thisMonth = today.getFullYear().toString() + ("0"+(today.getMonth()+1)).slice(-2)
            let TargetMonth = this.$route.params['target']
            this.thisMonth = thisMonth
            this.TargetMonth = TargetMonth
            this.host = process.env.VUE_APP_API_BASE_URL;
            this.userinfo = JSON.parse(sessionStorage.getItem("user"))
            await ListStatusAPI.getTaskMaster(this)
            await ListStatusAPI.getStatusData(this,TargetMonth)
        },
        ChangeState(event){
            let id = event.target.id;
            let flg = event.target.className;
            let changeFlg = (flg=="未") ? true:false
            let updateData = {toDoFlg:changeFlg}
            api.patch(this.host+"/ExState/"+id+"/update/",updateData)
            this.$router.go(this.$route.path)
        },
        SearchMonth(){
            if(this.TargetMonth.length==6){
                let month = this.TargetMonth.slice(-2) -1
                if(month >=0 && month <= 11)
                {
                    if(this.thisMonth==this.TargetMonth)
                    {
                        this.$router.replace({path:'/MainPage/'})
                    }else{
                        this.$router.replace({path:'/SearchMonth/'+this.TargetMonth})
                    }
                }
            }
        }
        ,
    },
};
</script>
