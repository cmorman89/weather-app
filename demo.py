from flask import Flask

app = Flask(__name__)

# Provide a route to the home page
@app.route("/")
def home():
    return "Success: Weather App is running."

if __name__ == "__main__":
    app.run(debug=True)