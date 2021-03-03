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
            toDoDatas:[],
            DeptList:[],
        }
    },
    created(){
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.userinfo = JSON.parse(sessionStorage.getItem("user"));
        this.getTaskMaster();
        this.getDepts();
        this.getStatusData("202103");
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
            api.get(this.host+"/GetDeptsMaster/")
            .then((response)=>{
                let List = []
                let dept_length = response.data.length
                for(let counter=0;counter<dept_length;counter++){
                    let data = response.data[counter]
                    List.push(data["id"])
                }
                this.DeptList = List
                console.log(this.DeptList)
            });
        },
        getStatusData(month){
            for(let counter=0;this.DeptList.length;counter++){
                let select_dept = this.DeptList[counter]
                api.get(this.host+"/ExState/"+month+"/"+select_dept+"/list/")
                .then((response)=>{
                    console.log(response)
                });
            }
        },
    }
};
</script>