# Weather API Logger (Scheduled)

## Description
Fetches weather data from an API and saves it into a CSV file repeatedly.

It extracts:
- City name
- Date
- Temperature (C)
- Humidity
This is a basic automation script that simulates real-world data logging.

## Modules Used
- `requests` – fetch API data
- `datetime` – get current date
- `pandas` – store data in CSV
- `pathlib` – manage file paths

## Output
```
Enter City Name (or 'q' to quit): hyderabad

------------------------------
City: hyderabad
Results: {'city': 'hyderabad', 'date': '2026-03-31', 'temp_C': '31', 'humidity': '28'}
Saved to: D:\Sabir Hussain Balal\Python\Projects\Beginner\python-web-network-projects\09_\data\data.csv
------------------------------

Enter City Name (or 'q' to quit): karachi

------------------------------
City: karachi
Results: {'city': 'karachi', 'date': '2026-03-31', 'temp_C': '28', 'humidity': '62'}
Saved to: D:\Sabir Hussain Balal\Python\Projects\Beginner\python-web-network-projects\09_\data\data.csv
------------------------------


Enter City Name (or 'q' to quit): q
Exiting...
```

## Features
- Accepts city input
- Fetches weather data from API
- Saves results to CSV
- Appends new data to existing file
- Handles errors and timeouts
- Loop until exit



## Project Structure
```
09_weather_api_logger/
├── data/
│ └── data.csv
├── main.py
└── README.md
```

## Notes
- Uses free API from wttr.in (no API key needed)
- Data is appended on each run (builds history)
- Some fields may be missing depending on API response
- Focus is on automation and data collection
