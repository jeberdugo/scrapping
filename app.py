from urllib.request import urlopen
import time
import requests
import re
from bs4 import BeautifulSoup
import telebot
from flask import Flask
app = Flask(__name__)
bot = telebot.TeleBot('5463548406:AAHtVHVSj6BM7oPl3aocs-wvs2oMMJ9b7cw')
num = 1
boletas = set()
@app.route('/')
def hello_world():
    while(num > 0):
        url = "https://pasala.checkout.tuboleta.com/selection/resale/item?performanceId=10228476815898"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        title_index = html.find("There")
        if(title_index > -1):
            global boletas
            print("Hay boletas")
            soup = BeautifulSoup(html, "html.parser")
            texto = ""
            tags = soup.find_all('div',{'class':'seat-info-category-legend'})
            for tag in tags:
                for name in tag.find_all('span',{'class':'name'}):
                    texto += name.text
                    texto += "\n"
                for price in tag.find_all('span',{'class':'int_part'}):
                    texto += price.text 
                    texto += "\n"
            if(boletas != tags):
                bot_send_text(texto)
                bot_send_text2(texto)
                bot_send_text3(texto)
                print("Hay cambios")
            else:
                print("No hay cambios")
            
            boletas = tags


        else:
            print("No hay boletas")
        
        time.sleep(30)

    return 'Hello, World!'

@app.route('/stop')
def hello_world2():
    num = -1
    return 'Stop'

@app.route('/init')
def hello_world3():
    num = 1
    return 'init'

@bot.message_handler(commands=['start'])
def bot_send_text(bot_message):
    bot.send_message("1033058635",bot_message+"https://pasala.checkout.tuboleta.com/selection/resale/item?performanceId=10228476815898")

@bot.message_handler(commands=['start'])
def bot_send_text2(bot_message):
    bot.send_message("623018232",bot_message+"https://pasala.checkout.tuboleta.com/selection/resale/item?performanceId=10228476815898")

@bot.message_handler(commands=['start'])
def bot_send_text3(bot_message):
    bot.send_message("5660600061",bot_message+"https://pasala.checkout.tuboleta.com/selection/resale/item?performanceId=10228476815898")



