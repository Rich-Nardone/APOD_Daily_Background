import requests
import json
import struct
import ctypes
from datetime import date
SPI_SETDESKWALLPAPER = 20
d = str(date.today())
PATH = 'C:\\Users\\Rich\\Desktop\\Picture_of_Day\\pic'+d+'.jpg'
key = 'YOUR_KEY_HERE'
Account_Email = 'YOUR_EMAIL_HERE'
Account_ID = 'YOUR_ACCOUNT_ID_HERE'
url = 'https://api.nasa.gov/planetary/apod?api_key='+key

def changeBG(PATH):
    """Change background depending on bit size"""
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
response = requests.get(url)
r = response.json()["hdurl"]
Picture_request = requests.get(r)
if Picture_request.status_code == 200:
    with open(PATH, 'wb') as f:
        f.write(Picture_request.content)
changeBG(PATH)
