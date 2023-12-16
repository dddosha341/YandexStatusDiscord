import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from pypresence import Presence
import time as TIME

browser = webdriver.Chrome()

url = 'https://music.yandex.ru/home'
browser.get(url)

print('Input your Discord App ID')

RPC = Presence(str(input()))
RPC.connect()
print('Starting...')

StartTime = TIME.time()

while True:
    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    try:
        artistNameData = soup.findAll(class_='d-link deco-link')
        artistName = ""
        for data in artistNameData:
            if not "Яндекс" in data:
                artistName += data
        songName = soup.findAll(class_='d-link deco-link track__title')[-1].text
        link = 'https://music.yandex.ru' + soup.findAll(class_='d-link deco-link track__title')[-1]['href']
        
        BTNS = [
        {
            "label": "Yandex Music",
            "url": f"{link}"
        }
        ]
        RPC.update(
            state = f"{artistName} - {songName}",
            details = "Слушает то, что ему нравится",
            start = StartTime,
            buttons = BTNS,
            large_image = "main",
            small_image = 'small_image',
            small_text = 'Круче только я',
            large_text = "дадада")
    except:
        pass    
    
    TIME.sleep(1)

