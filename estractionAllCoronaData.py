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


#database connection

connection = sqlite3.connect("Coron")

cursor = connection.cursor()
#sql= "CREATE TABLE IF NOT EXISTS `CoronaVirus20` ( `id` int(11) NOT NULL,`Positivi` int(11) NOT NULL,`Deceduti` int(11) NOT NULL,`Guariti` int(11) NOT NULL,`Data_reg` datetime NOT NULL, PRIMARY KEY (`id`))"
sql = "CREATE TABLE IF NOT EXISTS 'All_CoronaVirus20_Datas' ('Positivi'	INTEGER NOT NULL,'Deceduti'	INTEGER NOT NULL, 'Guariti'	INTEGER NOT NULL, 'Data_reg' TEXT NOT NULL);"
cursor.execute(sql)

'''
main_url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
req = requests.get(main_url)
stringReq = req.text
jsonReq = json.loads(stringReq);
for singleDay in jsonReq:
    print(singleDay['deceduti'])
    sql_insert = "INSERT INTO All_Coronavirus20_Datas(Positivi, Deceduti, Guariti, Data_reg) VALUES(" + str(singleDay['totale_positivi']) + ", "  + str(singleDay['deceduti']) + ", " + str(singleDay['dimessi_guariti']) + ", '" + str(singleDay['data']) +"');"
    print(sql_insert)
    ##sys.exit()
    cursor.execute(sql_insert)
    connection.commit()
'''

sql_select = "SELECT * FROM All_Coronavirus20_Datas"
cursor.execute(sql_select)

morti = ()
posit = ()
tempo = ()
#result = cursor.fetchone()
rows = cursor.fetchall()
for row in rows:
    morti += (row[1],)
    posit += (row[0],)
    tempo += (row[3],)
  

x = tempo
y = morti
plt.plot(x, y, marker = "o", color = 'red')
plt.title("Andamento morti da CoronaVirus20")
plt.xlabel("Tempo") 
plt.ylabel("Dececuti")
plt.show()

