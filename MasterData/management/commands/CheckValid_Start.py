from django.core.management import BaseCommand
import requests,json,datetime
from . import settings
class Command(BaseCommand):

    def add_arguments(self,parser):
        thisDate = datetime.date.today().strftime('%Y%m%d')
        parser.add_argument('targetDate',nargs='?',default=thisDate)
    
    def loginConnect(self,url,uid,password):
        '''ログインしてaccessトークンを取得する
        この際にbufferに出力してresponseのaccessトークンを取得する
        '''
        login_header = {'Content-Type':'application/json','Accept':'application/json'}
        login_data = json.dumps({"user_id":uid,"password":password})
        response = requests.post(url,headers=login_header,data=login_data)
        if response.status_code == 200:
            text = response.text
            data= json.loads(text)
            return data['access']
        else:
            return ''
    
    def DeptValidCheck(self,token,TargetDate):
        year = TargetDate[0:4]
        month = TargetDate[4:6]
        day = TargetDate[6:8]
        targetString = year + "-" + month + "-" + day
        header = {'Content-Type':'application/json','Authorization':'JWT '+token,'Accept':'application/json'}
        response = requests.post('http://localhost:8000/api/v1/MasterControll/getDepts/checkValid/'+targetString+'/',headers=header)
        if response.status_code == 200:
            self.stdout.write('DEPT変更成功')
        else:
            self.stdout.write('DEPT変更失敗')
    
    def TaskValidCheck(self,token,TargetDate):
        year = TargetDate[0:4]
        month = TargetDate[4:6]
        day = TargetDate[6:8]
        targetString = year + "-" + month + "-" + day
        header = {'Content-Type':'application/json','Authorization':'JWT '+token,'Accept':'application/json'}
        response = requests.post('http://localhost:8000/api/v1/MasterControll/getTasks/checkValid/'+targetString+'/',headers=header)
        if response.status_code == 200:
            self.stdout.write('TASK変更成功')
        else:
            self.stdout.write('TASK変更失敗')


    def handle(self,*args,**options):
        year = int(options['targetDate'][0:4])
        month = int(options['targetDate'][4:6])
        day = int(options['targetDate'][6:8])
        uid = settings.UID
        password = settings.PASSWORD
        targetDate = options['targetDate']
        if ( len(targetDate)==8 and (month<=12 and month >=1) and (day>=1 and day<=31) ):
            checkDate = datetime.date(year,month,day)
            if (checkDate.year==year and checkDate.month == month and checkDate.day==day):
                login_url = 'http://localhost:8000/api/v1/auth/jwt/create'
                login_token = self.loginConnect(login_url,uid,password)
                if not login_token =="":
                    self.stdout.write(login_token)
                    self.DeptValidCheck(login_token,targetDate)
                    self.TaskValidCheck(login_token,targetDate)
                else:
                    self.stdout.write('ログインできませんでしたIDとパスワードを確認してください')
            else:
                self.stdout.write('YYYYMM形式で入力してください')
        else:
            self.stdout.write('YYYYMM形式で入力してください') 