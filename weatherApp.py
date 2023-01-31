import requests
import key

city = "Razgrad"

url = f"api.openweathermap.org/data/2.5/forecast?id=524901&appid={key.key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve weather data.")