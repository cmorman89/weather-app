import requests
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


# Provide a route to the home page
@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        api_key = os.getenv("API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": city.title(),
                "temperature": round(data["main"]["temp"]),
                "icon": data["weather"][0]["icon"],
                "type": data["weather"][0]["main"].title(),
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
            }
        else:
            error = f"City '{city}' not found. Please try again."

    return render_template("home.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
