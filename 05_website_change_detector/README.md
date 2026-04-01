# Website Change Detector

## Description
Detects if a website has changed by comparing its current content with previously saved data.
Saves a hash of the website content and compares it on next runs.

It shows:
- HTTP status code
- Change detection (updated or not)
- Saves website hash for future checks

## Modules Used
- `requests` – send HTTP requests
- `hashlib` – create hash of content
- `pathlib` – handle file paths

## Output
```
Enter URL (or 'q' to quit): asd
Request Error: HTTPSConnectionPool(host='asd', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("HTTPSConnection(host='asd', port=443): Failed to resolve 'asd' ([Errno 11001] getaddrinfo failed)"))

Enter URL (or 'q' to quit): sabirhusseinbalal.github.io

------------------------------
URL: https://sabirhusseinbalal.github.io
Status: 200
Website saved for tracking.
------------------------------


Enter URL (or 'q' to quit): sabirhusseinbalal.github.io

------------------------------
URL: https://sabirhusseinbalal.github.io
Status: 200
No changes detected.
------------------------------


Enter URL (or 'q' to quit): sabirhusseinbalal.github.io

------------------------------
URL: https://sabirhusseinbalal.github.io
Status: 200
Website updated!
------------------------------


Enter URL (or 'q' to quit): q
Exiting...
```

## Features
- Detects website changes automatically
- Saves content for future comparison
- Handles errors and timeouts
- Loop until exit


## Project Structure
```
05_website_change_detector/
├── data/ # Stores saved website hashes
├── main.py
└── README.md
```

## Notes
- First run will save the website
- Next runs will compare changes
- Works based on HTML content changes
