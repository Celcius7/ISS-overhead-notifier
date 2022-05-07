import requests
import datetime as dt
MY_LAT = 24.792480
MY_LNG = 85.007713
response = requests.get(url= "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude= data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
iss_position = (latitude, longitude)
print(iss_position)

parameters = {
    'lat':MY_LAT,
    'lng':MY_LNG,
    'formatted': 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

now = dt.datetime.now()
print(now.hour)



