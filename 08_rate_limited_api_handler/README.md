# Rate-Limited API Handler (Retry / Backoff)

## Description
Handles API rate limits by detecting "429 Too Many Requests" responses and retrying the request after waiting.
It uses a simple retry system with increasing wait time (backoff).

It handles:
- Successful responses (200)
- Rate-limited responses (429)
- Other errors (404, 500, etc.)

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
- Accepts URL input from user
- Detects rate limiting (429 status)
- Retries request with increasing delay
- Stops retrying after max attempts
- Handles normal and error responses
- Measures total time taken
- Loop until user exits
- Simple and beginner-friendly logic



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
