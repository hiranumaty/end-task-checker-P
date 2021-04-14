class InputCheckAPI{
    
    input_check(id,name,DateString){
        var flg = false
        if(this.id_check(id))
            if(this.name_check(name))
                if(this.Date_check(DateString))
                    flg = true
        return flg
    }
    id_check(id){
        var flg = false;
        //idは5桁の数字
        const stringpattern = "^[0-9]{5}$";
        if(id.match(stringpattern)){
            flg = true
        }
        return flg
    }
    name_check(name){
        var flg = false;
        //名前は30文字以内
        if(name.length>=1 && name.length<=30){
            flg = true
        }
        return flg
    }
    Date_check(DateString){
        var flg = false;
        //4桁-2桁-2桁で入力
        const stringpattern = "^[0-9]{4}-[0-9]{2}-[0-9]{2}$";
        if(DateString.match(stringpattern))
        {
            var year = DateString.split("-")[0]
            var month = DateString.split("-")[1]
            var day = DateString.split("-")[2]
            var checkdate = new Date(year,month,day)
            if(checkdate.getFullYear()==year && checkdate.getMonth()==month&&checkdate.getDate()==day)
            {
                flg = true   
            }
        }
        return flg
    }
}
export default InputCheckAPI