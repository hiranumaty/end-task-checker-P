import requests,json,datetime
from django.core.management import BaseCommand
from . import settings
class Command(BaseCommand):
    #起動引数を取得したい
    def add_arguments(self,parser):
        '''起動引数の設定
        TargetMonth (任意のパラメーター)　YYYYMM形式で入力
        uid ログイン用UID #python-dotenvを適用せよ
        pass ログイン用パスワード #python-dotenvを適用せよ
        '''
        thisMonth = datetime.date.today().strftime('%Y%m')
        parser.add_argument('TargetMonth',nargs='?',default=thisMonth)

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

    def ExRegist(self,token,yearmonth):
        #ここが止まらない問題is 何
        Ex_header = {'Content-Type':'application/json','Authorization':'JWT '+token,'Accept':'application/json'}
        response = requests.post('http://localhost:8000/api/v1/ExState/CreateState/'+yearmonth+'/',headers=Ex_header)
        if response.status_code == 200:
            return True
        else:
            return False

    def handle(self,*args,**options):
        year = int(options['TargetMonth'][0:4])
        month = int(options['TargetMonth'][4:6])
        day = 1
        if(len(options['TargetMonth'])==6 and (month<=12 and month >=1)):
            checkDate = datetime.date(year,month,day)
            if (checkDate.year==year and checkDate.month == month):
                uid = settings.UID
                password = settings.PASSWORD
                login_url = 'http://localhost:8000/api/v1/auth/jwt/create'
                login_token = self.loginConnect(login_url,uid,password)
                if  not login_token == "":
                    self.ExRegist(login_token,options['TargetMonth'])
                else:
                    self.stdout.write('ログインできませんでしたIDとパスワードを確認してください')
            else:
                self.stdout.write('YYYYMM形式で入力してください')
        else:
            self.stdout.write('YYYYMM形式で入力してください') 