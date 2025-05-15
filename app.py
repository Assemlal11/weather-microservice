from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "31ef068a7d1d409190d200137251505"

@app.route('/forecast')
def forecast():
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location is required"}), 400

    # Call WeatherAPI.com for a 5-day forecast
    weather_url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=5"
    response = requests.get(weather_url)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    if response.status_code != 200:
        return jsonify({"error": "Weather API error", "details": response.text}), 500

    try:
        data = response.json()
        forecast_days = data.get("forecast", {}).get("forecastday", [])
    except Exception as e:
        return jsonify({"error": "Invalid JSON", "details": str(e)}), 500

    forecast_list = []

    for day in forecast_days:
        forecast_list.append({
            "date": day["date"],
            "temperature_high": round(day["day"]["maxtemp_f"]),
            "temperature_low": round(day["day"]["mintemp_f"]),
            "wind_speed_avg": round(day["day"]["maxwind_mph"]),
            "precipitation": round(float(day["day"]["daily_chance_of_rain"]))
        })

    return jsonify(forecast_list)

if __name__ == '__main__':
    app.run(debug=True)
