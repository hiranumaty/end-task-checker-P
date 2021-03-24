import api from './api'
class AdminListApi{
    getTaskMaster(parent){
        let taskList = [];
        api.get(parent.host+"/GetTaskMaster/")
        .then((response)=>{
            for(let counter=0;counter<response.data.length;counter++)
            {
                let data = response.data[counter]
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
                DeptList.push(data)
            }
        });
        return DeptList
    }
}
export default AdminListApi