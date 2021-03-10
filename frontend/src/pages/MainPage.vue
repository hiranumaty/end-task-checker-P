<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <table>
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
                        <button v-if="cell.id!=''" :id="cell.id">変更</button>
                    </td>
                </template>
            </tr>
           </template>
        </table>
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
    async created(){
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.userinfo = JSON.parse(sessionStorage.getItem("user"))
        await this.getTaskMaster()
        await this.getStatusData("202103")
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
                    List.push({text:data["Task_name"],value:"Column"+(counter+1)})
                }
                this.taskLength = column_Length;
                this.taskListColumns = List;
            });
        },
        getStatusData(month){
            let toDoDatas = new Array();
            let DeptList = new Array();
            toDoDatas = [];
            DeptList = [];
            api.get(this.host+"/GetDeptsMaster/")
            .then((response)=>{
                let dept_length = response.data.length
                for(let counter=0;counter<dept_length;counter++){
                    let data = response.data[counter]
                    DeptList.push(data["id"])
                }
                for (let key in DeptList){
                    api.get(this.host+"/ExState/"+month+"/"+DeptList[key]+"/list/")
                    .then((response)=>{
                        let data =  response.data
                        let item = {}
                        console.log(data)
                        for (let dtcounter=0;dtcounter<data.length;dtcounter++){
                            if(dtcounter==0){
                                item["Column"+dtcounter] = {text:data[dtcounter]["deploy_name"],id:""}
                            }
                            let text = (data[dtcounter]["toDoFlg"] == true) ? "済":"未"
                            let link_id = data[dtcounter]["id"]
                            item["Column"+(dtcounter+1)] = {text:text,id:link_id}
                        }
                        console.log(item)
                        toDoDatas.push(item)
                    });
                }
                this.toDoDatas = toDoDatas
                this.DeptList = DeptList
            });
                
        },
    }
};
</script>