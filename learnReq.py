import requests as r
from secret import key

city=str(input("Enter city name:"))

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+key

response = r.get(url)
print(response.status_code)

data = response.json()
temp1 = data['main']['temp']

print(temp1)