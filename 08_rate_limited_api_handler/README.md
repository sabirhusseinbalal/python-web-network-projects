# Rate-Limited API Handler (Retry / Backoff)

## Description
Handles API rate limits by detecting "429 Too Many Requests" responses and retrying the request after waiting.
It uses a simple retry system with increasing wait time (backoff).

It handles:
- Successful responses (200)
- Rate-limited responses (429)
- Other errors (404, 500, etc.)

**YouTube Video:**
[[Rate-Limited API Handler | Web, Network & API Automation (Project 8)](https://youtu.be/OYvbxNX31oI/)]

## Modules Used
- `requests` – send HTTP requests
- `time` – handle delays and measure time

## Output
```
Enter URL (or 'q' to quit): https://httpbin.org/status/429
Rate limited. Retrying in 1s...
Rate limited. Retrying in 2s...
Rate limited. Retrying in 3s...
Rate limited. Retrying in 4s...

------------------------------
Requested URL: https://httpbin.org/status/429
Tries: 4
Final Status: 429
Time Elapsed: 14.79 seconds
------------------------------


Enter URL (or 'q' to quit): https://httpbin.org/status/200

------------------------------
Requested URL: https://httpbin.org/status/200
Tries: 1
Final Status: 200
Time Elapsed: 1.19 seconds
------------------------------


Enter URL (or 'q' to quit): https://httpbin.org/status/404

------------------------------
Requested URL: https://httpbin.org/status/404
Tries: 1
Final Status: 404
Time Elapsed: 1.18 seconds
------------------------------


Enter URL (or 'q' to quit): q
Exiting...
```

## Features
- Accepts URL input
- Automatically retries on rate limit (429)
- Increases wait time between retries
- Displays total attempts and time
- Handles errors and timeouts
- Loop until exit


## Project Structure
```
08_rate_limited_api_handler/
├── main.py
└── README.md
```

## Notes
- APIs may block too many requests using status code 429
- This project uses simple linear backoff (1s, 2s, 3s...)
- Real systems may use exponential backoff
- Stops retrying after a fixed number of attempts
