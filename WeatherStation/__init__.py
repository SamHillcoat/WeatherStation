from flask import Flask, request, render_template, g
import json
import sqlite3 as sql
import csv
import datetime, time

app = Flask(__name__)
DATABASE = '/var/www/FlaskApp/FlaskApp/weather.db'								#Server
#DATABASE = '/home/sam/Programming/weather-station/FlaskApp/FlaskApp/weather.db' #Local
windspeed_jsonfile = "/var/www/FlaskApp/FlaskApp/static/windspeed.json"

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def insert_readings(windspeed, temp):
	with sql.connect(DATABASE) as con:
		cur = con.cursor()
		cur.execute("INSERT INTO weather_readings (time, windspeed, temperature) VALUES(datetime(CURRENT_TIMESTAMP, 'localtime'), ?, ?)", (windspeed, temp,))
		con.commit()

def write_to_csv(query, output):
	with sql.connect(DATABASE) as con:			#CHANGE DATABASE BEFORE UPLOADING TO SERVER
		cur = con.cursor()
		cur.execute(query)   
		with open(output, "wb") as csv_file:              # Python 2 version
			deleteContent(csv_file)
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow([i[0] for i in cur.description]) # write headers
			csv_writer.writerows(cur)

def write_to_json(data, jsonfile):
    time_now = datetime.datetime.now()
    now = time_now + datetime.timedelta(hours=11)
    for_js = int(time.mktime(now.timetuple())) * 1000
    #write = {str(now):data}
    #result = json.dumps(write)
    with open(jsonfile, 'w') as outfile:
        outfile.write('['+str(for_js)+','+data+']')



#def write_file(windspeed):
#	with open('/var/www/FlaskApp/FlaskApp/POST.txt', 'a') as file:
#		fo.write('\n', windspeed)

query_windspeed = "SELECT time, windspeed FROM weather_readings WHERE time BETWEEN datetime('now','localtime', '-1 minute') AND datetime('now', 'localtime')"
csv_windspeed = "/var/www/FlaskApp/FlaskApp/static/windspeed.csv"
@app.route("/", methods=['GET','POST'])
def result():
	if request.method == 'POST':
		windspeed = request.form['windspeed']
		temp = request.form['temp']			
		insert_readings(windspeed, temp)
		#write_to_csv(query_windspeed, csv_windspeed)
		write_to_json(windspeed, windspeed_jsonfile)
		return "Successful Insert"
	else:
		return render_template('index.html')
@app.route("/data")
def data():
	temp = request.args.get('temp')
	windspeed = request.args.get('windspeed')
	insert_readings(windspeed, temp)
	write_to_json(windspeed, windspeed_jsonfile)
	return "Successful Insert"
		


#@app.route("/windspeed.csv", methods=['GET', 'POST'])
#def


if __name__ == "__main__":
    app.run(debug=True)
