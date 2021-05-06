import os 
from os.path import join ,dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(os.getcwd(),'.env')
load_dotenv(dotenv_path)

UID = os.environ.get('UID')
PASSWORD = os.environ.get('PASSWORD')