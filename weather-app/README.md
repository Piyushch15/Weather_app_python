# Weather App (Python + Tkinter)

A simple **desktop weather application** built using **Python, Tkinter GUI**, and **OpenWeatherMap API**.  
It fetches real-time weather details (temperature, humidity, and condition) for any city and displays them with a clean interface and background image.

> Built by **Piyush Channote (Piyushch15)**. MIT Licensed.

---

## ✨ Features
- Search weather by city name.
- Displays temperature (°C), weather description, and humidity.
- Customizable background image.
- Uses OpenWeatherMap API for live weather data.

---

## 🛠️ Requirements
- Python 3.x
- Libraries: `tkinter`, `requests`, `Pillow`

Install dependencies:
```bash
pip install requests pillow
```

---

## 🚀 Usage
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Replace `api_key` in the code with your key.
3. Run:
```bash
python src/weather_app.py
```
4. Enter a city name and click **Get Weather**.

---

## 📂 Project Structure
```
weather-app/
├─ src/
│  └─ weather_app.py
├─ assets/
│  └─ (background image)
├─ docs/
│  └─ usage.md
├─ .github/
│  └─ ISSUE_TEMPLATE/
│     ├─ bug_report.md
│     └─ feature_request.md
├─ LICENSE
├─ README.md
```

---

## 🐞 Troubleshooting
- **City not found:** Check spelling or try another city.
- **Failed to retrieve weather data:** Verify internet connection and API key.
- **Image not loading:** Ensure correct path for background image.

---

## 🗺️ Roadmap
- Add weather icons dynamically.
- Show more details (wind speed, feels like).
- 5-day forecast version.

---

## 🤝 Contributing
Contributions are welcome! Fork the repo, make changes, and submit a PR.

---

## 📄 License
MIT © 2025 Piyush Channote
