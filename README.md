# 🌤️ Weather Forecast Microservice (Microservice A)

This microservice provides a 5-day weather forecast (including temperature, wind speed, and precipitation) for a sailboat race application. It uses the OpenWeatherMap API to retrieve weather data for a specified location.

## 🔧 Setup Instructions

1. Clone the repo and navigate into the project folder.
2. Install required Python packages:

   pip install -r requirements.txt

3. Add your OpenWeatherMap API key to a `.env` file in the root directory:

   OPENWEATHERMAP_API_KEY=your_api_key_here

4. Run the Flask app:

   python app.py

   The server will start at: http://127.0.0.1:5000/

## 📡 API Endpoint

### GET `/forecast`

**Example:**

http://127.0.0.1:5000/forecast?location=Newport,OR&date=2025-05-17

### Parameters:
- `location` (required): City and state abbreviation (e.g., Newport,OR)
- `date` (optional): Format YYYY-MM-DD. If omitted, returns the full 5-day forecast.

## ✅ Sample JSON Response

[
  {
    "date": "2025-05-15",
    "precipitation": 0,
    "temperature_high": 54,
    "temperature_low": 47,
    "wind_speed_avg": 8
  },
  {
    "date": "2025-05-16",
    "precipitation": 0,
    "temperature_high": 54,
    "temperature_low": 50,
    "wind_speed_avg": 6
  },
  {
    "date": "2025-05-17",
    "precipitation": 89,
    "temperature_high": 52,
    "temperature_low": 50,
    "wind_speed_avg": 13
  },
  {
    "date": "2025-05-18",
    "precipitation": 86,
    "temperature_high": 54,
    "temperature_low": 44,
    "wind_speed_avg": 13
  },
  {
    "date": "2025-05-19",
    "precipitation": 85,
    "temperature_high": 58,
    "temperature_low": 40,
    "wind_speed_avg": 8
  }
]

## 💻 Example Python Usage

```python
import requests

url = "http://127.0.0.1:5000/forecast?location=Newport,OR"
response = requests.get(url)

if response.status_code == 200:
    forecast = response.json()
    for day in forecast:
        print(f"Date: {day['date']}, High: {day['temperature_high']}°F, Low: {day['temperature_low']}°F, Precipitation: {day['precipitation']}%, Wind Speed: {day['wind_speed_avg']} mph")
else:
    print("Failed to get forecast.")
---

## 📊 UML Sequence Diagram

This diagram shows the interaction between your main program, the microservice, and the OpenWeatherMap API:

![uml-sequence](https://github.com/user-attachments/assets/6056548e-3217-413c-9b21-c3c98501f1b9)


### Sequence Summary:
1. **Main Program** sends a GET request to `/forecast`
2. **Microservice** sends request to **OpenWeatherMap API**
3. **OpenWeatherMap** returns weather data
4. **Microservice** sends back formatted JSON to the Main Program
