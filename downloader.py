import requests 
from bs4 import BeautifulSoup 
import urllib.request
import os
import getpass

user = getpass.getuser()
#вставляем ответ xhr запроса формата txt с данными и подключаемся к ним
#для теста https://audio-lib.club/wp-content/uploads/playlists/transerfing-realnosti-i-v-stupeni.txt
txt = ""
def EnterUrl():
    url = input(" введите ссылку xhr запроса > ")
    if url[-3:] == "txt":
        print("успех")
        html = requests.Session().get(url).content
        soup = BeautifulSoup(html, "lxml")#данные прео бразуем в ссылки и названия
        global txt
        txt = soup.text.replace('file', '').replace('title', '').replace('}', '').replace('{', '').replace(' ', '').replace('"', ' ').replace(':', '').replace(',', '').replace('https', ' https:').split()
    else:
        print("ошибка ввода")
        EnterUrl()
        url = ""
EnterUrl()

#распределяем по соответсвующим спискам
fileName = []
fileLinks = []

for l in txt[0::2]:
    fileLinks.append(l)
for n in txt[1::2]:
    fileName.append(n)

#создание папки для хранения mp3
dir = "C://Users/"+user+"/Desktop/books/"
namedir = str(0)
#для созадния разных папок для книг
n = 1
m = 999
for n in range(0,m):
    if os.path.exists(dir + namedir):
        namedir = str(n)
    else:
        if os.path.exists(dir):
            print("Books уже создана")
        else:
            print("создал папку 'Books'")
            os.mkdir(dir)
        os.mkdir(dir + namedir)
        break

#Загрузка книги с ресурса
i=0 
for download in fileLinks[1:]:
    r = requests.get(download)
    if r :
        print("загрузил: " + fileName[i])
        urllib.request.urlretrieve(download, dir + namedir + '/' + fileName[i]  + ".mp3")
    else:
        print("error " + r.status_code + fileName[i])
    i+=1