import datetime
import pycurl,json,ast
from django.core.management import BaseCommand
from io import BytesIO
class Command(BaseCommand):
    #起動引数を取得したい
    def add_arguments(self,parser):
        '''起動引数の設定
        TargetMonth (任意のパラメーター)　YYYYMM形式で入力
        uid ログイン用UID
        pass ログイン用パスワード
        '''
        thisMonth = datetime.date.today().strftime('%Y%m')
        parser.add_argument('TargetMonth',nargs='?',default=thisMonth)
        parser.add_argument('uid')
        parser.add_argument('pass')
    def loginConnect(self,url,uid,password):
        '''ログインしてaccessトークンを取得する
        この際にbufferに出力してresponseのaccessトークンを取得する
        '''
        buffer = BytesIO()
        login_header = ['Content-Type:application/json','Accept:application/json']
        login_data = json.dumps({"user_id":uid,"password":password})
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL,url)
        curl.setopt(pycurl.HTTPHEADER,login_header)
        curl.setopt(pycurl.POST,True)
        curl.setopt(pycurl.POSTFIELDS,login_data)
        curl.setopt(pycurl.WRITEDATA,buffer)
        curl.perform()
        response = curl.getinfo(pycurl.HTTP_CODE)
        if response == 200:
            response = buffer.getvalue()
            data= json.loads(response)
            return data['access']
        else:
            return ''
    def handle(self,*args,**options):
        year = int(options['TargetMonth'][0:4])
        month = int(options['TargetMonth'][4:6])
        day = 1
        if(len(options['TargetMonth'])==6 and (month<=12 and month >=1)):
            checkDate = datetime.date(year,month,day)
            if (checkDate.year==year and checkDate.month == month):
                uid = options['uid']
                password = options['pass']
                login_url = 'http://localhost:8000/api/v1/auth/jwt/create'
                login_token = self.loginConnect(login_url,uid,password)
                print(login_token)
            else:
                self.stdout.write('YYYYMM形式で入力してください')
        else:
            self.stdout.write('YYYYMM形式で入力してください') 