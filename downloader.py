import requests 
from bs4 import BeautifulSoup 
import urllib.request
import os
import getpass
import json
from time import sleep 
USER = getpass.getuser()
#вставляем ответ xhr запроса формата txt с данными и подключаемся к ним
#для теста https://audio-lib.club/wp-content/uploads/playlists/transerfing-realnosti-i-v-stupeni.txt
txt = ""
def EnterUrl():
    url = input(" введите ссылку xhr запроса > ")
    if url[-3:] == "txt":
        print("успех")
        global txt
        html = requests.Session().get(url).content
        soup = BeautifulSoup(html, "lxml").text
        txt = soup.replace("[","").replace("]","").replace(" ","").replace("},","} ").split()
    else: 
        print("ошибка ввода")
        EnterUrl()
        url = ""
EnterUrl()

#распределяем по соответсвующим спискам
fileName = []
fileLinks = []
keytitle = "title"
keyfile = "file"
#переводим с json в списки
for l in txt:
    obj = json.loads(l)
    if keytitle in obj:
        print(obj[keytitle])
        fileName.append(obj[keytitle])
    if keytitle in obj:
        fileLinks.append(obj[keyfile])
        print(obj[keyfile])

#создание папки для хранения mp3
dir = "C://Users/"+USER+"/Desktop/books/"
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
    sleep(1)
    if r :
        print("загрузил: " + fileName[i])
        urllib.request.urlretrieve(download, dir + namedir + '/' + fileName[i]  + ".mp3")
    else:
        print("error " +str(r.status_code) + fileName[i])
    i=i+1