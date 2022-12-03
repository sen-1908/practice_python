import requests
from bs4 import BeautifulSoup


token = "アクセストークン"
url = "https://notify-api.line.me/api/notify"

tenki_url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
responce = requests.get(tenki_url)
BeautifulSoup(responce.text, "html.parser")

headers = {"Authorization" : "Bearer "+ token}
content = {"message":"test"}

requests.post(url,headers=headers,data=content)