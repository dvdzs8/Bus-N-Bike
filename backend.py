import pandas as pd
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCsZtPMyYcUXHFbuDfSiePn_nr52hOaeZE")
model = genai.GenerativeModel("gemini-1.5-pro")

from fileinput import filename
from flask import Flask
app = Flask(__name__)

@app.route('/upload', methods = ['POST'])
def success():
    if request.method == 'POST':
        files = request.files.getlist("file")

        for i in files:
            i.save(i.filename)

        if "bus.csv" in files and "bike.csv" in files:
            bus_file = genai.upload_file("bus.csv", display_name="Bus Data")
            bike_file = genai.upload_file("bike.csv", display_name="Bike Data")
            result = model.generate_content(["Attached are the bike ride data from the rideshare services and bus stop usage data. Which bus stops are used frequently that do not have a bike rack near them?", bus_file, bike_file])

        elif "bike.csv" in files:
            bike_file = genai.upload_file("bike.csv", display_name="Bike Data")
            result = model.generate_content(["Attached are the bike ride data from the rideshare services. What bike racks should be added and upgraded?", bike_file])

        return result

if __name__ == '__main__':
    app.run()
