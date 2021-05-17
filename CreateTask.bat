@echo off
set date_str = %date:~-10,4%%date:~-5,2%
rem python manage.py makeExState %date_str%
pipenv run python3 manage.py makeExState %date_str%