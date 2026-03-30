# Website Change Detector

## Description
Checks if a website has changed by comparing its current content with previously saved data.
This project sends a request to a website, creates a hash of its content, and compares it with an old saved version.
If the content is different, it means the website has changed.


It shows:
- Status code
- Change detection (updated or not)
- Saves website automatically for future checks

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
- Accepts URL input from user
- Automatically fixes URL format
- Detects website changes using hash comparison
- Saves website data for future checks
- Handles request errors and timeouts
- Loop until user exits
- Simple and beginner-friendly logic


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
