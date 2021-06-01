#!/bin/bash
today=`date "+%Y%m"`
pipenv run python3 manage.py makeExState ${today}