import requests
import json
from bs4 import BeautifulSoup
import re
import time
import sys


def idget(url):
  id = url.split('?')[0].split('/')[-1]
  return id

def mediaUrlGet(shredurl):
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/103.0.2'}
  r = requests.get(shredurl,headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')
  link_tags = soup.find('link', {'data-react-helmet': 'true', 'rel': 'alternate', 'hreflang': 'ar-AR'})
  url = link_tags.get('href')
  r = requests.get(url,headers=headers)
  id = idget(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  next_data = soup.find('script', id='__NEXT_DATA__').string
  json_data = json.loads(next_data)
  
  jsonirls = json_data["props"]["pageProps"]["story"]["snapList"]
  
  for g in jsonirls:
    if g['snapId']['value'] == id:
      mediaUrl = g['snapUrls']['mediaUrl']
      break
  return mediaUrl
  



headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/103.0.2'}


url = "https://www.snapchat.com/add/jyny/jcDYwDWzSP6uWxuWCzEJyQAAgZ3VodGd3Z256AY8a_pzjAY8a_nhXAAAAAA?invite_id=ntLzJuBs&locale=ar_KW&share_id=AeeJlkp6S5mlPansJ4UHsw&sid=12bd2fd25db147998d4788ac8013c0aa"



id = url.split('?')[0].split('/')[-1]



vid = 'H3m1p73SQXW259IHsniNBgAAgYnh0cGhqbWN0AY8aW96NAY8aW9FeAAAAAA'
"""
html = '<script id="__NEXT_DATA__" type="application/json">{"key": "value"}</script>'

soup = BeautifulSoup(r.text, 'html.parser')

next_data = soup.find('script', id='__NEXT_DATA__').string
json_data = json.loads(next_data)

jsonirls = json_data["props"]["pageProps"]["story"]["snapList"]

for g in jsonirls:
  if g['snapId']['value'] == id:
    mediaUrl = g['snapUrls']['mediaUrl']
    
    print(g['snapIndex'])








def download(url,theTime=None):
  r = requests.get(url, stream=True, headers=headers)
  if "image" in r.headers['Content-Type']:
    if time:
      file_name = time.strftime('%Y.%m.%d.%H.%M.%S', time.gmtime(seconds))+ ".jpeg"
    else:
      file_name = r.headers['ETag'].replace('"', '') + ".jpeg"
    print(file_name)
  elif "video" in r.headers['Content-Type']:
    if time:
      file_name = time.strftime('%Y.%m.%d.%H.%M.%S', time.gmtime(seconds))+'.mp4'
    else:
      file_name = r.headers['ETag'].replace('"', '') + ".mp4"
    print(file_name)
    if os.path.isfile(file_name):
      sys.exit('Erorr: The file name is exits')
    sleep(0.3)
    if r.status_code == 200:
      with open(file_name, 'wb') as f:
        for chunk in r:
          f.write(chunk)





'''
%%===== For debugging =====%%

print()
with open('data.json','w',encoding='utf-8') as fp:
  json.dump(jsonirls,fp,indent=4, separators=(',', ':'))


with open("index.html","w") as fp:
  fp.write(str(soup))



'''
"""