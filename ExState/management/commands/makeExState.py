import datetime
import pycurl,json,ast
from django.core.management import BaseCommand
from io import BytesIO
class Command(BaseCommand):
    #起動引数を取得したい
    def add_arguments(self,parser):
        thisMonth = datetime.date.today().strftime('%Y%m')
        parser.add_argument('TargetMonth',nargs='?',default=thisMonth)
        parser.add_argument('uid')
        parser.add_argument('pass')
    def handle(self,*args,**options):
        year = int(options['TargetMonth'][0:4])
        month = int(options['TargetMonth'][4:6])
        day = 1
        if(len(options['TargetMonth'])==6 and (month<=12 and month >=1)):
            checkDate = datetime.date(year,month,day)
            if (checkDate.year==year and checkDate.month == month):
                #ログインURL
                login_url = 'http://localhost:8000/api/v1/auth/jwt/create'
                login_header = ['Content-Type:application/json','Accept:application/json']
                login_data = json.dumps({"user_id":options['uid'],"password":options['pass']})
                curl = pycurl.Curl()
                curl.setopt(pycurl.URL,login_url)
                curl.setopt(pycurl.HTTPHEADER,login_header)
                curl.setopt(pycurl.POST,True)
                curl.setopt(pycurl.POSTFIELDS,login_data)
                curl.perform()
                response = curl.getinfo(pycurl.HTTP_CODE)
                if response == 200:
                    data = BytesIO()
                    dictionary_data = json.dumps(str(data.getvalue()))
                    dictionary_str = json.loads(dictionary_data)[0]
                    print(dictionary_str)
                    #ここからどうやって辞書にすればいいの
                else:
                     self.stdout.write('ログインID またはpasswordが間違っています')
            else:
                self.stdout.write('YYYYMM形式で入力してください')
        else:
            self.stdout.write('YYYYMM形式で入力してください') 