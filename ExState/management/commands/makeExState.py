import datetime
import pycurl,json,ast
from django.core.management import BaseCommand
from io import BytesIO
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
        buffer = BytesIO()
        login_header = ['Content-Type:application/json','Accept:application/json']
        login_data = json.dumps({"user_id":uid,"password":password})
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL,url)
        curl.setopt(pycurl.HTTPHEADER,login_header)
        curl.setopt(pycurl.POST,True)
        curl.setopt(pycurl.POSTFIELDS,login_data)
        curl.setopt(pycurl.WRITEDATA,buffer)
        curl.setopt(pycurl.CONNECTTIMEOUT,10)
        curl.perform()
        response = curl.getinfo(pycurl.HTTP_CODE)
        curl.close()
        if response == 200:
            response = buffer.getvalue()
            data= json.loads(response)
            buffer.close()
            return data['access']
        else:
            return ''
    def ExRegist(self,token,yearmonth):
        #ここが止まらない問題is 何
        buffer = BytesIO()
        curl = pycurl.Curl()
        Ex_header = ['Content-Type:application/json','Authorization:JWT '+token,'Accept:application/json']
        curl.setopt(pycurl.URL,'http://localhost:8000/api/v1/ExState/CreateState/'+yearmonth+'/')
        curl.setopt(pycurl.HTTPHEADER,Ex_header)
        curl.setopt(pycurl.WRITEDATA,buffer)
        curl.setopt(pycurl.POST,True)
        curl.setopt(pycurl.TIMEOUT_MS,500)
        curl.perform()
        curl.close()
        #ここで何を待っているんだ?
        #response = curl.getinfo(pycurl.HTTP_CODE)
        # if response == 200:
        #     print('作成が完了しました')
        #     return True
        # else:
        #     print('作成失敗です')
        #     return False
        #HTTPステートを取得して結果を出したいけれど...なぜかおわらない


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
                    sys.exit()
                else:
                    print('ログインできませんでしたIDとパスワードを確認してください')
            else:
                self.stdout.write('YYYYMM形式で入力してください')
        else:
            self.stdout.write('YYYYMM形式で入力してください') 