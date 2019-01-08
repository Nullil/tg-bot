# -*- coding: utf-8 -*-
import redis
import os
import telebot
from selenium import webdriver # $ pip install selenium
#from selenium.webdriver.common.desired_capabilites import desired_capabilites
from bs4 import BeautifulSoup
#import time
#from ghost import Ghost
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
# import requests
# user_id = 12345
# url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
# r = requests.get(url)
# with open('test.html', 'w') as output_file:
#   output_file.write(r.text.encode('cp1251'))

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# get chromedriver from 
# https://sites.google.com/a/chromium.org/chromedriver/downloads


def get_all_championship(html):
    soup = BeautifulSoup(html, 'lxml')
    #print(len(match_list))
    champ = soup.find_all('div', class_='c-events__item_head')
    # link = soup.find_all('ul', class_='liga_menu ')[4].find_all('a')

    # link_match_name = []
    # for link_1 in link:
    #     link_match_name.append(link_1.get('href').split('/')[2])
    # print(link_match_name)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # print(len(link_match_name))



        
    match_champ_name = []
    for ch in champ:

        #parent = ch.next
        #print(parent)
        champ_name = ch.find('div', class_='c-events__name').text.strip()
        champ_url = ch.find('div', class_='c-events__name').find('a').get('href')
        
        #print(champ_url)######
        
    
    
    match = soup.find_all('div', class_='c-events-scoreboard')
    for mat in match:
        url_match = mat.find('div', class_='c-events-scoreboard__item').find('a').get('href')
        match_champ_name.append(url_match.split('/')[2])
        

        match_name = mat.find('span', class_='c-events__teams').get('title')
        #print(match_name)####
        scoreboard = mat.find('div', class_='c-events-scoreboard__lines').find_all('div', class_='c-events-scoreboard__line')
        score1 = scoreboard[0].find_all('span', class_="c-events-scoreboard__cell")
        score2 = scoreboard[1].find_all('span', class_="c-events-scoreboard__cell")
        spis1 = []
        spis2 = []
        for sco in score1:
            spis1.append(sco.text)
        for sco in score2:
            spis2.append(sco.text)
        #print(spis1)###
        #print(spis2)###
        #print(match_list)
        unik = True
        match_1 = Match(match_name,url_match,spis1,spis2)
        for mat in match_list:
            if (match_1 == mat):
                unik = False
            else:
                mat.update(spis1,spis2)
        if (unik):
            match_list.append(match_1)

    for mat in match_list:
        pass
        #mat.display_info()###
        #analytics(mat)


    
    #asArray(match_champ_name, link_match_name)

class Match:
    def __init__(self, match_name, url_match, score1, score2):
        self.match_name = match_name
        self.url_match = 'https://1xstavka.ru/' + url_match
        self.score1 = score1
        self.score2 = score2
        self.set = int(score1[0]) + int(score2[0])
        self.was_show = False
    def update(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        self.set = int(score1[0]) + int(score2[0])
    def show(self):
        self.was_show = True
    def display_info(self):
        print(self.match_name + '\n' + self.url_match)
        print(self.score1)
        print(self.score2)
        print()
    def __eq__(self, other):
        return self.url_match == other.url_match

# def analytics(match):#message,
#     if (not match.was_show):
#         if (match.set >= 2):
#             if ((int(match.score1[1]) + int(match.score2[1]) >= 45) & (int(match.score1[2]) + int(match.score2[2]) >= 45)):
#                 match.show()
#                 print(match.match_name)# в будущем это будет вывод в телеграмм
#                 #bot.send_message(message.chat.id, m.match_name + "\n" + m.url_match)


def stav():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('window-size=1920x935')
    # browser = webdriver.Chrome(chrome_options=options)
    # browser.get(url)
    url = "https://1xstavka.ru/live/Volleyball/"
    path = R"D:\Downloads\chromedriver_win32\chromedriver.exe"
    browser = webdriver.Chrome(path)
    #browser.add_argument('--headless')
    browser.get(url)
    
    html = browser.page_source
    browser.quit()
    get_all_championship(html)

    #//////
    #ghost = Ghost()
    #page, resources = ghost.open(url)
    #print(resources)
    #/////

def main():
    bot = telebot.TeleBot(token)
    #bot.send_message(503237630, "Kyky")
    #для этого скрипта нужно подрубать впн
    while True:
                stav()
                for m in match_list:
                    analytics(message, m)
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        answer = "Hi"
        if message.text == "hi":
            bot.send_message(message.chat.id, answer)
        #elif message.text == "Do":
        elif "Do" == "Do":
            while True:
                stav()
                for m in match_list:
                    analytics(message, m)
                    # if (m.was_show == False):
                    #     bot.send_message(message.chat.id, m.match_name + "\n" + m.url_match)
        else:
            bot.send_message(message.chat.id, message.text)
    def analytics(message,match):#
        if (not match.was_show):
            if (match.set >= 2):
                if ((int(match.score1[1]) + int(match.score2[1]) >= 45) & (int(match.score1[2]) + int(match.score2[2]) >= 45)):
                    match.show()
                    print(match.match_name)# в будущем это будет вывод в телеграмм
                    bot.send_message(message.chat.id, match.match_name + "\n" + match.url_match)
    #time.sleep(10)
    bot.polling(none_stop=True, interval=0)

    

    
match_list = []# хранятся все матчи
if __name__ == '__main__':
    print('+')
    main()




