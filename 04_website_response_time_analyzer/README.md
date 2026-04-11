# Website Response Time Analyzer

## Description
Measures how fast a website responds by sending multiple HTTP requests and calculating the average response time.

It shows:
- Requested URL
- HTTP status code
- Average response time

**YouTube Video:**
[[Website Response Time Analyzer | Web, Network & API Automation (Project 4)](https://youtu.be/enutauD290U/)]

## Modules Used
- `requests` – send HTTP requests
- `time` – measure execution time

## Output
```
Enter URL (or 'q' to quit): www.google.com

------------------------------
Requested URL: https://www.google.com
Status Code: 200
Average time: 1.10 seconds
------------------------------


Enter URL (or 'q' to quit):
```

## Features
- Accepts URL input
- Fixes missing `https://`
- Sends multiple requests
- Calculates average response time
- Handles errors
- Loop until exit


## Project Structure
```
04_website_response_time_analyzer/
├── main.py
└── README.md
```

## Notes
- Response time varies with network conditions
- Focus is on performance measurement
