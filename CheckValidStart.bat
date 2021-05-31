@echo off
set date_str = %date:~-10,4%%date:~-5,2%%date:~-2,2%
pipenv run python3 manage.py CheckValid_Start %date_str%