# Weather App Demo

This app will fetch the current weather (temperature, humidity, precipitation) for a given location.
Uses the OpenWeatherMap API to fetch 

---

- [Weather App Demo](#weather-app-demo)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Contact](#contact)

---

## Setup

1. Clone the repo.
    ```
    git clone https://github.com/cmorman/weather-app
    ```
2. Change directory:
    ```
    cd weather-app
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Enter your API key:
    ```
    echo "API_KEY = <replace-with-your-api-key>" > .env
    ```
    > [!IMPORTANT]
    > - Replace `<your_api_key_here>` with your actual [API key](https://home.openweathermap.org/api_keys).

    > [!NOTE]
    > - Create a free account at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) is required to obtain an [API key](https://home.openweathermap.org/api_keys).

5. Run the app: 
    ```
    python demo.py
    ```

---

## Usage
1. Navigate to http://127.0.0.1:5000
2. Enter the target city and click "Get Weather"

---

## Contact

github@cmorman.com