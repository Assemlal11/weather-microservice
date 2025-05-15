from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

@app.route('/forecast')
def forecast():
    location = request.args.get('location')
    date_str = request.args.get('date')

    if not location:
        return jsonify({"error": "Location is required"}), 400

    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=imperial"
    response = requests.get(weather_url)

    if response.status_code != 200:
        return jsonify({"error": "Weather API error"}), 500

    data = response.json()["list"]

    forecast_list = []
    dates_seen = set()

    for entry in data:
        dt_txt = entry["dt_txt"]
        dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
        date = dt.date().isoformat()

        if date_str and date != date_str:
            continue
        if date not in dates_seen and dt.hour == 12:
            forecast_list.append({
                "date": date,
                "temperature_high": round(entry["main"]["temp_max"]),
                "temperature_low": round(entry["main"]["temp_min"]),
                "wind_speed_avg": round(entry["wind"]["speed"]),
                "precipitation": round(entry.get("pop", 0) * 100)
            })
            dates_seen.add(date)

        if len(forecast_list) == 5:
            break

    return jsonify(forecast_list)

if __name__ == '__main__':
    app.run(debug=True)
