
from flask import Flask, render_template
import requests
import time

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('index.html')

@app.route("/<location>")
def weather(location):
	#Parameters for the API to find the location ID
	parameters = {
		"query": location
	}
	#Request the API to get the location id
	id_response = requests.get("http://metaweather.com/api/location/search/", params=parameters,verify=False)
	#Get the id from the response
	id = (id_response.json()[0])['woeid']
	print(id)
	#Request the API to get the weather based on location id
	weather_response = requests.get("http://metaweather.com/api/location/" + str(id))
	#converting to JSON
	weather_json = weather_response.json()
	#Get the consolidated weather from the JSON file
	consolidated_weather = weather_json['consolidated_weather']
	#Get the list of weather info for today weather
	today_weather = consolidated_weather[0]
	#Get today temperature from the list
	today_temp = today_weather['the_temp']
	print(today_temp)
	#Render the result on HTML file
	return render_template('weather.html', location=location, temp=today_temp)



if __name__=="__main__":
	app.run(host='0.0.0.0', port=8080)
