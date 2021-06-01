#!/bin/bash
today=`date "+%Y%m%d"`
pipenv run python3 manage.py CheckValid_Start ${today}