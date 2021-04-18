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


#connection = pymysql.connect(host="MarcoDev93.mysql.pythonanywhere-services.com", port="3306", user="MarcoDev93", passwd="Superbalo93", database="MarcoDev93$coronavirus")
#connection = pymysql.connect(host="localhost", user="root", passwd="", database="CoronaVirus")
#connection = sqlite3.connect("CoronaVirus")
connection = sqlite3.connect("Coron")

cursor = connection.cursor()
#sql= "CREATE TABLE IF NOT EXISTS `CoronaVirus20` ( `id` int(11) NOT NULL,`Positivi` int(11) NOT NULL,`Deceduti` int(11) NOT NULL,`Guariti` int(11) NOT NULL,`Data_reg` datetime NOT NULL, PRIMARY KEY (`id`))"
sql = "CREATE TABLE IF NOT EXISTS 'CoronaVirus20' ('id'	INTEGER NOT NULL,'Positivi'	INTEGER NOT NULL,'Deceduti'	INTEGER NOT NULL, 'Guariti'	INTEGER NOT NULL, 'Data_reg'	TEXT NOT NULL, PRIMARY KEY('id'));"
cursor.execute(sql)

# queries for retrievint all rows
conta_id = "SELECT COUNT(id) FROM CoronaVirus20;"

#executing the quires
cursor.execute(conta_id)
rows = cursor.fetchall()

for row in rows:
    numero_id = row[0]
    print(row[0])
    id = row[0]


main_url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json"
req = requests.get(main_url)

stringReq = req.text
jsonReq = json.loads(stringReq);


print(jsonReq[0]['deceduti'])             #deceduti
print(jsonReq[0]['totale_positivi'])      #positivi
print(jsonReq[0]['dimessi_guariti'])      #guariti



#sys.exit()


id_int = id
id_int += 1


data = time.strftime("%Y-%m-%d")
ora = time.strftime("%H:%M:%S")
dateTime = data + " " + ora


# queries for retrievint all rows

sql_insert = "INSERT INTO CoronaVirus20(id, Positivi, Deceduti, Guariti, Data_reg) VALUES(" + str(id_int) + ", " + str(jsonReq[0]['totale_positivi']) + ", "  + str(jsonReq[0]['deceduti']) + ", " + str(jsonReq[0]['dimessi_guariti']) + ", '" + dateTime +"');"
print(sql_insert)
cursor.execute(sql_insert)
connection.commit()

sql_select = "SELECT * FROM Coronavirus20"
cursor.execute(sql_select)

morti = ()
posit = ()
tempo = ()
#result = cursor.fetchone()
rows = cursor.fetchall()
print(rows)
for row in rows:
    morti += (row[2],)
    posit += (row[1],)
    tempo += (row[4],)
    #print(morti)
    print(row)

print(morti)
print (posit)


x = tempo
y = morti

#x = np.linspace(-(2*np.pi), 2*np.pi, 100) 
#y = np.sin(x)


plt.plot(x, y, marker = "o", color = 'red')
plt.title("Andamento CoronaVirus20")
plt.xlabel("Tempo") 
plt.ylabel("Dececuti")
plt.show()