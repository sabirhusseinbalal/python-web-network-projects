# API Data Collector (JSON → CSV)

## Description
Fetches data from an API and saves it into a CSV file.
This project sends a request to an API, receives JSON data, and converts it into a structured CSV file for easy use.

It supports both:
- List of records
- Single JSON object


## Modules Used
- `requests` – send HTTP requests
- `pandas` – handle and convert data
- `pathlib` – manage file paths
- `shutil` – manage folders

## Output
```
Enter URL (or 'q' to quit): https://api.github.com/users/sabirhusseinbalal
Output folder exists. Delete and continue? (y/n): y
Processing 1 record(s)...

------------------------------
URL: https://api.github.com/users/sabirhusseinbalal
Status: 200
               login         id       node_id                                         avatar_url gravatar_id  ... public_gists followers following            created_at            updated_at
0  sabirhusseinbalal  246732079  U_kgDODrTVLw  https://avatars.githubusercontent.com/u/246732...              ...            0         0         0  2025-11-28T16:54:45Z  2026-02-24T05:53:41Z

[1 rows x 33 columns]
CSV saved to: D:\Sabir Hussain Balal\Python\Projects\Beginner\python-web-network-projects\06_api_data_collector_json__to_csv\output\data.csv
------------------------------


Enter URL (or 'q' to quit): https://api.github.com/users/sabirhusseinbalal_Loser!
Output folder exists. Delete and continue? (y/n): y
Processing 1 record(s)...

------------------------------
URL: https://api.github.com/users/sabirhusseinbalal_Loser!
Status: 404
     message             documentation_url status
0  Not Found  https://docs.github.com/rest    404
CSV saved to: D:\Sabir Hussain Balal\Python\Projects\Beginner\python-web-network-projects\06_api_data_collector_json__to_csv\output\data.csv
------------------------------


Enter URL (or 'q' to quit):
```

## Features
- Accepts API URL input
- Uses basic authentication
- Displays JSON response
- Handles errors and timeouts
- Loop until exit


## Project Structure
```
06_api_data_collector_json__to_csv/
├── output/
│ └── data.csv
├── main.py
└── README.md
```

## Notes
- Works best with public APIs
- JSON structure may vary between APIs
- Focus is on understanding API data handlings
- Even if API returns an error (like 404), the response may still be valid JSON
- In this case, the program will still convert and save that data into CSV
- Always check the status code before trusting the data
