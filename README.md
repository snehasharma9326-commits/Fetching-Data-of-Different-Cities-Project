# 🌦️ India Weather Data Analysis Using OpenWeatherMap API

A Python-based data analytics project that fetches **real-time weather data** for the **capital cities of Indian states** using the **OpenWeatherMap API**. The project processes the collected data, stores it in a Pandas DataFrame, and exports it to a CSV file for further analysis and visualization.

---

## 📖 Project Overview

This project demonstrates how to work with **REST APIs**, **JSON data**, and **data analysis** using Python.

The application automatically collects live weather information for all Indian state capitals and stores it in a structured format for future analysis.

---

## 🚀 Features

- 🌍 Fetches real-time weather data
- 🇮🇳 Covers all Indian state capitals
- 🌡️ Retrieves temperature information
- 🤗 Extracts "Feels Like" temperature
- 💧 Collects humidity levels
- 🌬️ Fetches wind speed
- ☁️ Retrieves cloud coverage
- 👀 Collects visibility data
- 📊 Retrieves atmospheric pressure
- 🌦️ Displays weather description
- 📁 Saves data into a CSV file
- 📈 Ready for Data Analysis & Visualization

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Pandas
- OpenWeatherMap API
- JSON
- Google Colab 

---

## 📂 Project Structure

```text
India-Weather-Data-Analysis/
│
├── API_WEATHER.ipynb
├── india_weather_data.csv
├── README.md
├── requirements.txt
└── images/
    └── weather_output.png
```

---

## 📊 Dataset Columns

The generated dataset contains the following columns:

| Column | Description |
|---------|-------------|
| State | Name of the Indian State |
| Capital | State Capital |
| Temperature | Current Temperature (°C) |
| Feels_Like | Feels Like Temperature |
| Humidity | Humidity (%) |
| Pressure | Atmospheric Pressure (hPa) |
| Weather | Weather Description |
| Wind_Speed | Wind Speed (m/s) |
| Clouds | Cloud Coverage (%) |
| Visibility | Visibility (meters) |

---

## 📌 Sample Output

| State | Capital | Temperature | Humidity | Weather |
|--------|----------|-------------|----------|----------|
| Madhya Pradesh | Bhopal | 30.5°C | 68% | Clear Sky |
| Maharashtra | Mumbai | 28.4°C | 82% | Broken Clouds |
| Rajasthan | Jaipur | 35.2°C | 40% | Sunny |

*(Values change because the API provides live weather data.)*

---

## 📡 API Used

This project uses the **OpenWeatherMap Current Weather API**.

Example API Request:

```text
https://api.openweathermap.org/data/2.5/weather?q=Bhopal&appid=YOUR_API_KEY&units=metric
```

---




---

## 📈 Project Workflow

```
OpenWeatherMap API
        │
        ▼
Fetch Live Weather Data
        │
        ▼
JSON Response
        │
        ▼
Extract Required Fields
        │
        ▼
Create Pandas DataFrame
        │
        ▼
Export to CSV
        │
        ▼
Data Analysis & Visualization
```

---

## 📚 Learning Outcomes

Through this project, I learned:

- REST API Integration
- Working with JSON Responses
- Data Collection using Python
- Pandas DataFrame Operations
- CSV File Generation
- Data Cleaning Basics
- Real-Time Data Handling
- Python Automation

---

## 🎯 Future Enhancements

- 📊 Interactive Dashboard using Streamlit
- 📈 Weather Trend Analysis
- 🌍 Multiple Country Support
- 🗺️ Weather Maps
- 📅 Historical Weather Data
- 📉 Advanced Data Visualization
- ☁️ Cloud Deployment

---


---

## 👩‍💻 Author

**Shalini Sharma**

🎓 B.Tech – Computer Science Engineering (Data Analytics)

💻 Passionate about Python, Data Analytics, APIs, and Machine Learning.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## ⭐ Support

If you found this project useful, don't forget to ⭐ **Star** this repository.

It motivates me to build more real-world Data Analytics and Python projects.

---

## 📜 License

This project is developed for educational and learning purposes.

---

> **"Real-time data transforms information into insights, and Python makes it possible."** 🚀
