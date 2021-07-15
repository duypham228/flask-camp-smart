
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('index.html')

@app.route("/<location>")
def weather(location):
	parameters = {
		"query": location
	}
	id_response = requests.get("http://metaweather.com/api/location/search/", params=parameters,verify=False)
	id = (id_response.json()[0])['woeid']
	print(id)
	weather_response = requests.get("http://metaweather.com/api/location/" + str(id))
	weather_json = weather_response.json()
	consolidated_weather = weather_json['consolidated_weather']
	today_weather = consolidated_weather[0]
	today_temp = today_weather['the_temp']
	print(today_temp)
	return render_template('weather.html', location=location, temp=today_temp)



if __name__=="__main__":
	app.run(host='0.0.0.0', port=8080)
