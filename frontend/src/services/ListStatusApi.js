import api from './api'
class ListStatusApi{
    getTaskMaster(parent){
        api.get(parent.host+"/GetTaskMaster/")
        .then((response) =>{
            let List = []
            List.push({ text: "部署名", value: "Column"+0})
            let column_Length = response.data.length
            for(let counter=0;counter<column_Length;counter++){
                let data = response.data[counter]
                List.push({text:data["Task_name"],value:"Column"+data["id"]})
            }
            parent.taskLength = column_Length;
            parent.taskListColumns = List;
        });
    }
    getStatusData(parent,month){
        let DeptList = new Array();
        DeptList = [];
        api.get(parent.host+"/GetDeptsMaster/")
        .then((response)=>{
            let dept_length = response.data.length
            for(let counter=0;counter<dept_length;counter++){
                let data = response.data[counter]
                DeptList.push(data["id"])
            }
            this.getStatusPart(parent,month,DeptList)
            .then(response =>{
                parent.toDoDatas = response
            });
            parent.DeptList = DeptList
        });
    }
    async getStatusPart(parent,month,DeptList){
        let toDoDatas = []
        for await(let DeptKey of DeptList){
            //ここが少し怪しいと思う（タスク有効無効の兼ね合いで)
            await api.get(parent.host+"/ExState/"+month+"/"+DeptKey+"/list/")
                .then((response)=>{
                    let data =  response.data
                    let item = {}
                    for(let TaskKey in parent.taskListColumns)
                    {
                        //存在しないデータを空白に初期化
                        let ColumnNo = parent.taskListColumns[TaskKey]["value"]
                        item[ColumnNo] = {text:"",id:""}
                    }
                    for (let dtcounter=0;dtcounter<data.length;dtcounter++){
                        //なぜ上書きにならずColumnColumnになるの
                        if(dtcounter==0){
                            item["Column"+dtcounter] = {text:data[dtcounter]["deploy_name"],id:""}
                        }
                        let text = (data[dtcounter]["toDoFlg"] == true) ? "済":"未"
                        let link_id = data[dtcounter]["id"]
                        item["Column"+data[dtcounter]["Task_id"]] = {text:text,id:link_id}
                    }
                    toDoDatas.push(item)
                });
        }
        return toDoDatas
    }
}
export default ListStatusApi