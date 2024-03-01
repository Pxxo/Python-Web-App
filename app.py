from flask import Flask, render_template
import requests
import json

getpos_URL = "https://get.geojs.io/v1/ip/geo.json"
data = requests.get(getpos_URL).json()
city = data['city']
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={
        # 緯度・軽度を指定する場合
        "lat": data['latitude'],
        "lon": data['longitude'],

        # 都市名で取得する場合
        # "q": "tokyo",
        # apikey
        "appid": 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        "units": "metric",
        "lang": "ja",
    },
)
ret = json.loads(response.text)

temp = ret['main']['temp']
temp_max = ret['main']['temp_max']
temp_min = ret['main']['temp_min']

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", temp=temp, temp_max=temp_max, temp_min=temp_min, city=city)


if __name__ == "__main__":
    app.run(debug=True)
