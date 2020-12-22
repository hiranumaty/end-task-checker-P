from django import forms

class LoginForm(forms.Form):
    #ログインフォーム
    user_id = forms.CharField()
    password = forms.CharField()