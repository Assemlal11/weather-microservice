import requests

url = "http://localhost:5000/forecast?location=Newport,OR&date=2025-05-17"
response = requests.get(url)

print("Weather Forecast:")
for day in response.json():
    print(day)
