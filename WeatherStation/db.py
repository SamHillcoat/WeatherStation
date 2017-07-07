from flask import g
import sqlite3 as sql
DATABASE = '/var/www/FlaskApp/FlaskApp/weather.db'

def insert_readings(windspeed,temp):
	with sql.connect(DATABASE) as con:
		cur = con.cursor()
		cur.execute("INSERT INTO weather_readings (windspeed,temperature) VALUES (?,?)", (windspeed,temp))
		con.commit()
windspeed = 12
temp = 23
insert_readings(windspeed,temp)
print ("DONE")

