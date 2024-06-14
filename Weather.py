import requests
import json
import os

city = input("Enter the name of your city \n")

url=f"https://api.weatherapi.com/v1/current.json?key=3210cd78c40a4352bd9114817230811&q={city}"
r = requests.get(url)
#print(r.text)

weatherdic= json.loads(r.text)

print(weatherdic["location"]["name"],weatherdic["location"]["region"],weatherdic["current"]["temp_c"])
temp=weatherdic["current"]["temp_c"]
say=f"The temperature of  {city} is {temp} degree celsius"

command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{say}');"
os.system(command)