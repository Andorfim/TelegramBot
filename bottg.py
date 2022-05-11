# -*- coding: utf-8 -*-
"""bottg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RHXZEh66l5Ums-VfOfmQpKW_ILzvqTyw
"""

!pip install pytelegrambotapi
!pip install lxml
!pip install requests
!pip install beautifulsoup4
!pip install fake_useragent
!pip install yfinance 
import telebot
from requests import get
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import yfinance as yf
import base64
from datetime import datetime
import matplotlib.pyplot as plt


UserAgent().chrome
bot = telebot.TeleBot('')
soup = ""

ticker = list = ["SNAP", "A","AA","AAL","AAP","AAPL","ABBV","ABT","ADBE","ADI","ADM","ADP","ADS","ADSK","AEE","AES",
"AFL","AIG","AIV","AIZ","AJG","AKAM","ALB","ALGN","ALK","ALL","ALXN","AMAT","AMD","AME","AMG","AMGN",
"AMP","AMT","AMZN","AN","ANSS","ANTM","APA","APD","APH","ARE","ARNC","ATVI","AVB",
"AVGO","AVY","AXP","AYI","AZO",
"BA","BAC","BAX","BBBY","BBY","BDX","BEN","BHF",
"BIIB","BK","BKNG","BLK","BLL","BMY","BRK-B","BSX","BWA","BXP",
"C","CAG","CAH","CAT","CBOE",
"CBRE","CCI","CERN","CF","CFG","CHD","CHK","CHRW","CHTR","CI","CINF","CL","CLF","CLX",
"CMA","CMCSA","CME","CMG","CMI","CMS","CNC","CNP","COF","COG","COO","COP","COST","COTY","CPB",
"CRM","CSCO","CTAS","CTSH","CTXS","CVS","CVX",
"DAL","DE","DFS","DG","DGX","DHI","DHR","DIS",
"DISCA","DISCK","DLR","DLTR","DNB","DRI","DTE","DVA","DVN","DXC",
"EA","EBAY","ECL","ED",
"EFX","EIX","EL","EMN","EMR","EOG","EQIX","EQT","ES",
"F","FAST","FB","FBHS","FCX","FDX","FE","FFIV","FIS","FISV","FITB",
"FL","FLR","FLS","FMC","FOX","FOXA","FSLR","FTV","GD","GE","GILD","GIS","GLW",
"GM","GOOG","GOOGL","GPC","GPN","GPS","GS","GT","GWW","HAL","HAS","HBAN","HBI","HCA","HD",
"HES","HIG","HLT","HOG","HOLX","HON","HP","HPE","HPQ","HRB","HRL","HSIC","HST","HSY","HUM",
"IBM","ICE","IDXX","IFF","ILMN","INCY","INTC","INTU","IP","IPG","IRM","ISRG","IT","ITW","JBHT","JNJ","JNPR","JPM","JWN","K","KEY","KHC","KIM","KLAC","KMB","KMI","KMX","KO","KR","KSU","L",
"LB","LEG","LEN","LEN-B","LH","LKQ","LLY","LMT","LNT","LOW","LRCX","LUV","M","MA",
"MAA","MAC","MAR","MAS","MAT","MCD","MCHP","MCK","MCO","MDLZ","MET","MHK","MKC","MLM","MMC","MMM",
"MNST","MO","MOS","MPC","MRK","MRO","MS","MSFT","MSI","MTB","MTD","MU","MUR","NAVI","NDAQ",
"NEE","NEM","NFLX","NKE","NOC","NOV","NRG","NSC","NTAP","NTRS","NUE","NVDA","NWL","NWS","NWSA",
"O","OI","OKE","OMC","ORCL","ORLY","OXY","PANW","PBCT","PBI","PCAR","PCG","PDCO","PEG","PEP","PFE","PFG",
"PG","PGR","PH","PHM","PKI","PLD","PM","PNC","PPG","PPL","PRU","PSA","PSX","PVH","PWR","PXD","PYPL","QCOM",
"QRVO","R","REG","REGN","RF","RHI","RJF","RL","ROK","ROP","ROST","RRC","RSG","SBUX","SCHW",
"SEE","SHW","SJM","SLG","SNA","SNPS","SO","SOHU","SPG","SPGI","SPLK","SQ","SRCL","SRE","STT","STZ","SWK",
"SWKS","SWN","SYF","SYK","SYY","T","TAP","TDC","TDG","TGNA","TGT","TJX","TMO","TPR","TRIP",
"TROW","TRV","TSCO","TSLA","TSN","TWTR","TXN","TXT","UA","UAA","UAL","UDR","UHS","ULTA","UNH","UNM",
"UNP","UPS","URBN","URI","USB","V", "VFC","VLO","VMC","VNO","VRSK","VRSN","VRTX","VTR","VZ","WAT",
"WBA","WDC","WEC","WELL","WFC","WHR","WM","WMB","WMT","WRK","WU","WY","WYNN","XEC","XEL","XLNX","XOM","XRAY","XRX","XYL","YUM","ZBH","ZION","ZTS"]

bukvsb = list = ["A", "B","C","D","E","F","G", "H", "E", "F","G","H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
bukvsm = list = []
i = 0 
for i in range(len(bukvsb)-1):
  bukvsm.append(bukvsb[i].lower())




@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id, '''Привет!
  Вот, что я умею: 
  -Рекомедации инвест-домов 
  -Собственная аналитика и рекомендация
  -Альтернативные акции
Введи тикер акции (без $) и наслаждайся!'''
  )

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  from fake_useragent import UserAgent
  UserAgent().chrome
  message.text = str(message.text)
  # bot.send_message(message.chat.id, message.text)
  # print(message.text)
  i = 0
  url1 = "https://finviz.com/quote.ashx?t="
  url2 = "&ty=c&ta=1&p=d"
  url1 = url1 + message.text + url2
  print(url1)
  page1 = requests.get(url1, headers={'User-Agent': UserAgent().chrome})
  soup = BeautifulSoup(page1.text, "html.parser")
  soup = str(soup)
  t = ""
  message.text = message.text.upper()
  proverka = str(message.text in ticker)
  if proverka == "True":
    def news(i):
      j = i
      g = "" 
      for h9 in range(3):
        g = g + soup[i]
        i += 1
      i = j
      return g
    def chisl(i):
      j = i 
      g = ""
      for h in range(3):
        g = g + soup[i]
        i += 1
      i = j
      return g

    def body(i):
      j = i
      g = ""
      for h in range(27):
        g = g + soup[i]
        i+=1
      i = j
      return g

    def body2(i):
      j = i
      g = ""
      for h in range(25):
        g = g + soup[i]
        i += 1
      i = j
      return g

    def td(i):
      j = i
      l = ""
      for h in range(2):
        l = l + soup[i]
        i += 1
      i = j
      return l

    def left(i):
      j = i 
      g = ""
      for h in range(4):
        g = g + soup[i]
        i += 1
      i = j
      return g

    c1 = 1
    # print(len(soup))
    for h in range(2):
      while i < len(soup)-28:
        if body(i) == "body-table-rating-downgrade" or body2(i) == "body-table-rating-neutral" or body2(i) == "body-table-rating-upgrade":
          break
        else:
          i += 1
      i += 1
    # print(i)

    if i == 0:
      i = 0 
      # print(i)
      for h in range(2):
        while i < len(soup)-28:
          print(61234786123748162934)
          if body2(i) == "body-table-rating-neutral" or body2(i) == "body-table-rating-upgrade":
            break
          else:
            i += 1
        i += 1
    # if i == 0:
    #   for h in range(2):
    #     while i < len(soup)-28:
    #       if body2(i) == "body-table-rating-upgrade":
    #         break
    #       else:
    #         i += 1
    #     i += 1

    # for h in range(50):
    #   t = t + soup[i]
    #   i += 1


    # print(i)
    for h in range(5):
      while td(i) != "td":
        i += 1
        if td(i) == "td":
          i += 1
          break



    # for h in range(50):
    #   t = t + soup[i]
    #   i += 1

    while soup[i] != ">":
      i += 1
    i += 1

    while soup[i] != "<":
      t = t + soup[i]
      i += 1

    t = t + "..."

    # while left(i) != "left":
    #   i += 1
    # i = i + 3

    for h in range(2):
      while soup[i] != ">":
        i += 1 
      i += 1

    # t = t + "..."

    while soup[i] != "<":
      t = t + soup[i]
      i += 1

    t = t + "..."


    for h in range(2):
      while soup[i] != ">":
        i += 1
      i += 1 

    while soup[i] != "<":
      t = t + soup[i]
      i += 1

    # t = t + "..."

    # for h in range(1):
    #   while soup[i] != "$":
    #     i += 1
    #   i += 1

    # i -= 1

    # while soup[i] != "<":
    #   t = t + soup[i]
    #   i += 1


    # for h in range(50):
    #   t = t + soup[i]
    #   i += 1

    def a(i):
      i = j
      i = i + 6
      g = ""
      g = soup[i]
      j = i
      return g
    o = "  "
    t = o + t + '''
      '''
    h5 = 1
    h7 = 1 
    # здесь фор по 7 раз 
    i = i + 5
    for h5 in range(7):
      for h7 in range(3):
        while left(i) != "left":
          i += 1
        i += 1
      i = i + 17
      while soup[i] != "<":
        t = t + soup[i]
        i += 1
      t = t + "..."
      j = i
      g = ""
      for h11 in range(4):
        g = g + soup[i]
        i += 1
      i = j
      if g == "news":
        j = i
        while soup[i] != ".":
          i -= 1
        g = ""
        j = 0
        while j != i:
          g = g + t[j]
          j += 1
        t = g 
        break 
        
      for h3 in range(2):
        while soup[i] != ">":
          i += 1
        i += 1
      while soup[i] != "<":
        t = t + soup[i]
        i += 1
      t = t + "..."
      while soup[i] != "$":
        i += 1 
      while soup[i] != "<":
        t = t + soup[i] 
        i += 1
        tr = str(soup[i] in bukvsb)
        trm = str(soup[i] in bukvsm)
        if tr == "True" or trm == "True":
          i = len(t)-1
          g = ""
          for h in range(2):
            while soup[i] != ".":
              i -= 1 
            i -= 1
          for j in range(i):
            g = g + t[j]
          break  
        if soup[i] == "n":
          break
      t = t + '''
      '''
      i += 1 
      

    print(t)
    # на пятом td




    # k = 0 
    # t = ""
    # while i <= len(soup)-5:
    #   if buy(i) == "Buy" and k != 1:
    #     i = i + 2
    #     k = 1
    #   if k == 1:
    #     break
    #   i += 1

    # body-table-rating-downgrade  
  else:
    bot.send_message(message.chat.id, "Введи тикер правильно")
  i = 0 
  today = datetime.now().date()
  a = yf.download(message.text, start="2021-09-01", end=today)
  fig = plt.figure()
  close = a["Close"]
  x = list = []
  for i in range(len(close)):
    x.append(i)
  plt.plot(x, close)
  plt.savefig('grafic.png')
  bot.send_message(message.chat.id, t)
  # photo=open('grafic.png')
  # bot.send_photo(message.chat.id, photo=photo)
  # для roa 
  # def roa(i):
  #   g = ""
  #   for hroa in range(9):
  #     g = g + soup[i]
  #     i += 1
  # i = 0 
  # while roa(i) != "title>ROA":
  #   i += 1
  # for hroa in range(2):
  #   while soup[i] != "%":
  #     i += 1
  #   i += 1
  # roa = ""
  # while soup[i] != ">":
  #   i-= 1
  # i += 1
  # roa = ""
  # while soup[i] != "%":
  #   roa = roa + soup[i]
  #   i += 1
  # bot.send_message(message.chat.id, roa)
bot.polling(none_stop=True)
# @bot.message_handler(content_types=['text'])


#вынести в отдельном блокноте весь соуп и проследить как работает поиск 


#<di
