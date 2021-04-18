from bs4 import BeautifulSoup
import requests
import pymysql
import time
import logging
import soupsieve
import css_parser
import sqlite3
import sys
import json
import numpy as np 
import matplotlib.pyplot as plt




main_url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
req = requests.get(main_url)

stringReq = req.text
jsonReq = json.loads(stringReq);


for singleDay in jsonReq:
    if singleDay == jsonReq[0]:
        print(singleDay['deceduti'])

        id_int = id
        id_int += 1
        sql_insert = "INSERT INTO CoronaVirus20(id, Positivi, Deceduti, Guariti, Data_reg) VALUES(" + str(id_int) + ", " + str(singleDay['totale_positivi']) + ", "  + str(singleDay['deceduti']) + ", " + str(singleDay['dimessi_guariti']) + ", '" + str(singleDay['data']) +"');"
        print(sql_insert)
        cursor.execute(sql_insert)
        connection.commit()



sys.exit()

print(jsonReq[0])            
print(jsonReq[0]['deceduti'])             #deceduti
print(jsonReq[0]['totale_positivi'])      #positivi
print(jsonReq[0]['dimessi_guariti'])      #guariti



#sys.exit()

