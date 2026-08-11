import requests
import json
from datetime import datetime,timedelta

start_date=datetime.now().strftime("%Y-%m-%d")
end_date=(datetime.now()+timedelta(days=7)).strftime("%Y-%m-%d")
lat=input("Enter latitude ")
lon=input("Enter longitude ")

url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&start_date={start_date}&end_date={end_date}"

response=requests.get(url)
data=response.json()
print(data)

with open("daily_data.json",'w') as f:
    json.dump(data,f,indent=4)