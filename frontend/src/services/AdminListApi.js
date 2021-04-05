import api from './api'
class AdminListApi{
    getTaskMaster(parent){
        let taskList = [];
        api.get(parent.host+"/GetTaskMaster/")
        .then((response)=>{
            for(let counter=0;counter<response.data.length;counter++)
            {
                let data = response.data[counter]
                data["valid_text"] = (data["valid_flg"] ? "有効":"無効")
                taskList.push(data)
            }
        });
        return taskList
    }
    GetDeptsMaster(parent){
        let DeptList =[];
        api.get(parent.host+"/GetDeptsMaster/")
        .then((response)=>{
            for(let counter=0;counter<response.data.length;counter++)
            {
                let data = response.data[counter]
                data["valid_text"] = (data["valid_flg"] ? "有効":"無効")
                DeptList.push(data)
            }
        });
        return DeptList
    }

    getDeptDetail(parent,id){
        //部署の詳細を取得する
        let DeptDetail=[];
        api.get(parent.host+"/MasterControll/getDepts/"+id+"/detail/")
        .then((response)=>{
            let DeptData = response.data
            DeptData['valid_text'] = (DeptData['valid_flg']? "有効":"無効")
            DeptDetail.push(DeptData)
        });
        return DeptDetail
    }
    getTaskDetail(parent,id){
        //タスクの詳細を取得する
        let TaskDetail =[];
        api.get(parent.host+"/MasterControll/getTasks/"+id+"/detail/")
        .then((response)=>{
            let TaskData = response.data
            TaskData['valid_text'] = (TaskData['valid_flg']?"有効":"無効")
            TaskDetail.push(TaskData)
        });
        return TaskDetail
    }
}
export default AdminListApi