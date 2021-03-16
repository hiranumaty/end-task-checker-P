<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <div name="SearchField">
            <input type="text" v-model="TargetMonth">
            <button @click="SearchMonth">検索</button>
        </div>
        <table>
            <tr class="header">
                <template v-for="Column in taskListColumns">
                    <th :key="Column.index">{{Column.text}}</th>
                </template>
            </tr>
           <template v-for="toDodata in toDoDatas">
            <tr :key="toDodata.index">
                <template v-for="cell in toDodata">
                    <td :key="cell.index" >
                        {{cell.text}}
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
            thisMonth:"",
            TargetMonth:"",
            taskLength:"",
            taskListColumns:[],
            DeptList:[],
            toDoDatas:[],
        }
    },
    async created(){
        let today = new Date();
        let thisMonth = today.getFullYear().toString() + ("0"+(today.getMonth()+1)).slice(-2)
        let TargetMonth = this.$route.params['target']
        this.thisMonth = thisMonth
        this.TargetMonth = TargetMonth
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.userinfo = JSON.parse(sessionStorage.getItem("user"))
        await this.getTaskMaster()
        await this.getStatusData(TargetMonth)
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
            let DeptList = new Array();
            DeptList = [];
            api.get(this.host+"/GetDeptsMaster/")
            .then((response)=>{
                let dept_length = response.data.length
                for(let counter=0;counter<dept_length;counter++){
                    let data = response.data[counter]
                    DeptList.push(data["id"])
                }
                //ここの領域を非同期させたい
                this.toDoDatas = this.getStatusPart(month,DeptList)
                this.DeptList = DeptList
            });
        },
        getStatusPart(month,DeptList){
            let toDoDatas = []
            for (let key in DeptList){
                    api.get(this.host+"/ExState/"+month+"/"+DeptList[key]+"/list/")
                    .then((response)=>{
                        let data =  response.data
                        let item = {}
                        for (let dtcounter=0;dtcounter<data.length;dtcounter++){
                            if(dtcounter==0){
                                item["Column"+dtcounter] = {text:data[dtcounter]["deploy_name"],id:""}
                            }
                            let text = (data[dtcounter]["toDoFlg"] == true) ? "済":"未"
                            let link_id = data[dtcounter]["id"]
                            item["Column"+(dtcounter+1)] = {text:text,id:link_id}
                        }
                        toDoDatas.push(item)
                    });
                }
            return toDoDatas
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
    }
};
</script>