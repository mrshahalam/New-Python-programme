"""
A Weather Forecasting App of the current date telling the information of the weather condition and temperature.
An App Developed Using Web Scraping Tool - BeautifulSoup
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

print("-----------------------")
print("WEATHER FORECASTING APP")
print("-----------------------")

result = requests.get("https://weather.com/weather/5day/l/JATY0018:1:JA")

weather_data = result.content

html = BeautifulSoup(weather_data, "html.parser")

# 1. Get Container of all weather forecasting data
weather_forecast_container = html.find_all("div", "twc-table-scroller")

# 2. Get all weather forecasting data in the container
weather_datas = weather_forecast_container[0].find_all("tr", "clickable closed")

print(len(weather_datas), "Days Weather Forecasting Data")

# Collecting information of first item
print("Period:", weather_datas[0].find("span", "date-time").text)
print("Description:", weather_datas[0].find("td", "description").text)

# Processing Temperature Data into a readable format
temp = weather_datas[0].find("td", "temp").text
temp_list = list(temp)
# print(temp_list)
new_temp_list = temp_list[:3] + ["/"] + temp_list[3:]
temperature = "".join(new_temp_list)
print("Temperature:", temperature)

# 3. Loop through each weather data. Serial starting from 1
for serial, weather_data in enumerate(weather_datas, 1):

    temp = weather_data.find("td", "temp").text
    temp_list = list(temp)

     # If temperature data is available, show the temperature; otherwise 'Not Available'
    if temp_list[0] == '-' and temp_list[1] == '-':
        temp_list[:2] = "NA"
        new_temp_list = temp_list[:2] + ["/"] + temp_list[2:]
    else:
        new_temp_list = temp_list[:3] + ["/"] + temp_list[3:]

    temperature = "".join(new_temp_list)

    # 4. Get each weather data
    print("{}. {} - {} - {}F\n".format(serial, weather_data.find("span", "date-time").text, weather_data.find("td", "description").text, temperature))

periods = [weather_data.find("span", "date-time").text for weather_data in weather_datas]
print(periods)
print(len(periods))

descriptions = [weather_data.find("td", "description").text for weather_data in weather_datas]
print(descriptions)
print(len(descriptions))

temperatures = [weather_data.find("td", "temp").text for weather_data in weather_datas]
print(temperatures)
print(len(temperatures))

result_final = pd.DataFrame(
    {
        "Period": periods,
        "Description": descriptions,
        "Temperature": temperatures,
    }
)

result_final.index += 1

result_final.to_csv(r"D:\Documents\5-day_weather_forecast.csv", header = True, index_label='Serial')
