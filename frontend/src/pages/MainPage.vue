<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <v-data-table
            :headers = "taskListColumns"
            :items = "toDoDatas"
        >
        </v-data-table>
    </v-app>
</template>
<script>
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import api from "@/services/api";
export default{
    components:{
        GlobalHeader,
        GlobalMessage,
    },
    data(){
        return{
            taskLength:"",
            taskListColumns:[],
            DeptList:[],
            toDoDatas:[],
        }
    },
    created(){
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.userinfo = JSON.parse(sessionStorage.getItem("user"))
        this.getTaskMaster()
        this.getStatusData("202103")
    },
    methods:{
        getTaskMaster(){
            api.get(this.host+"/GetTaskMaster/")
            .then((response) =>{
                let List = []
                List.push({ text: "部署名", value: "Column"+0})
                let column_Length = response.data.length
                for(let counter=0;counter<column_Length;counter++){
                    let data = response.data[counter]
                    List.push({text:data["Task_name"],value:"Column"+counter+1})
                }
                this.taskLength = column_Length;
                this.taskListColumns = List;
            });
        },
        getDepts(){
            let List = []
            api.get(this.host+"/GetDeptsMaster/")
            .then((response)=>{
                let dept_length = response.data.length
                for(let counter=0;counter<dept_length;counter++){
                    let data = response.data[counter]
                    List.push(data["id"])
                }
            });
            return List;
        },
        getStatusData(month){
            let DeptList = this.getDepts();
            console.log(DeptList)
            for(let dept in DeptList){
                api.get(this.host+"/ExState/"+month+"/"+dept+"/list/")
                .then((response)=>{
                    console.log(response)
                });
            }  
        },
    }
};
</script>