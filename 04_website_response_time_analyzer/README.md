# Website Response Time Analyzer

## Description
Measures how fast a website responds by sending multiple HTTP requests and calculating the average response time.

It shows:
- Requested URL
- HTTP status code
- Average response time

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
- Accepts URL input from the user
- Automatically fixes missing https://
- Sends multiple requests to improve accuracy
- Calculates average response time
- Displays clean output
- Handles request errors and timeouts
- Loop until user exits
- Simple and beginner-friendly logic


## Project Structure
```
04_website_response_time_analyzer/
├── main.py
└── README.md
```

## Notes
- Response time may vary due to network conditions
- Some websites may respond slower or block requests
- Focus is on understanding performance measurement
