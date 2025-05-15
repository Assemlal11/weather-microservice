import requests

# Define API endpoint and query parameters
url = "http://127.0.0.1:5000/forecast"
params = {
    "location": "Newport,OR",
    "date": "2025-05-17"
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises HTTPError for bad status codes

    try:
        data = response.json()
        print("Weather Forecast:\n")
        for day in data:
            print(f"Date: {day['date']}, "
                  f"High: {day['temperature_high']}°F, "
                  f"Low: {day['temperature_low']}°F, "
                  f"Precipitation: {day['precipitation']}%, "
                  f"Wind Speed: {day['wind_speed_avg']} mph")
    except ValueError:
        print("❌ Failed to decode JSON. Here's the raw response:")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
