@echo off
set date_str=%date:~-10,4%%date:~-5,2%
pipenv run manage.py makeExState %date_str%