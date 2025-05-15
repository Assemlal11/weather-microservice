# Weather Forecast Microservice (Microservice A)

This microservice provides a 5-day weather forecast (including temperature, wind speed, and precipitation) for a sailboat race application. It uses the OpenWeatherMap API to retrieve weather information for a given location.

---

## How to Request Data

Send a **GET** request to this endpoint:

```
http://localhost:5000/forecast?location=Newport,OR&date=2025-05-17
```

### Parameters:
- `location` (string, required): e.g., `"Newport,OR"`
- `date` (string, optional): `"YYYY-MM-DD"` — if omitted, you'll get the full 5-day forecast.

---

## What the Microservice Returns

A JSON array with 5 forecast entries like this:

```json
[
  {
    "date": "2025-05-17",
    "temperature_high": 68,
    "temperature_low": 54,
    "wind_speed_avg": 14,
    "precipitation": 10
  },
  {
    "date": "2025-05-18",
    "temperature_high": 70,
    "temperature_low": 56,
    "wind_speed_avg": 13,
    "precipitation": 5
  },
  {
    "date": "2025-05-19",
    "temperature_high": 67,
    "temperature_low": 52,
    "wind_speed_avg": 15,
    "precipitation": 25
  },
  {
    "date": "2025-05-20",
    "temperature_high": 66,
    "temperature_low": 50,
    "wind_speed_avg": 18,
    "precipitation": 15
  },
  {
    "date": "2025-05-21",
    "temperature_high": 64,
    "temperature_low": 49,
    "wind_speed_avg": 12,
    "precipitation": 0
  }
]
```

---

## Example Usage in Python

```python
import requests

url = "http://localhost:5000/forecast?location=Newport,OR&date=2025-05-17"
response = requests.get(url)
print(response.json())
```

---

## 📊 UML Sequence Diagram

This diagram shows the interaction between your main program, the microservice, and the OpenWeatherMap API:

![uml-sequence](https://github.com/user-attachments/assets/6056548e-3217-413c-9b21-c3c98501f1b9)


### Sequence Summary:
1. **Main Program** sends a GET request to `/forecast`
2. **Microservice** sends request to **OpenWeatherMap API**
3. **OpenWeatherMap** returns weather data
4. **Microservice** sends back formatted JSON to the Main Program
