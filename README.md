# 🌍 City Explorer

**City Explorer** is a Python CLI tool that lets you explore cities around the world by retrieving key information such as historical facts, population data, and current weather. It uses open APIs like Wikipedia and OpenWeatherMap.

## 🚀 Features

- Get a brief historical summary of any city
- Display country, population, and geographic info
- Show current weather and temperature
- Works directly from your terminal

## 🧰 Tech Stack

- Python 3
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [OpenWeatherMap API](https://openweathermap.org/api)
- `requests`, `wikipedia`, `argparse`, `dotenv`

## 🖥️ Example usage

```bash
$ python city_explorer.py "Nantes"
📍 City: Nantes, France
🌦 Weather: Partly cloudy, 18°C
🧠 History: Nantes is a city in western France, located on the Loire River...
