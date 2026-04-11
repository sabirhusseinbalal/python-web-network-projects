# Authenticated API Client (Bearer / Basic Auth)

## Description
Sends authenticated requests to APIs using Bearer tokens or Basic Authentication.
This project helps understand how APIs protect data and how clients send credentials securely.

It supports:
- Bearer Token (via headers)
- Basic Authentication (username & password)
This is an important step toward working with real-world APIs.

**YouTube Video:**
[[Authenticated API Client | Web, Network & API Automation (Project 7)](https://youtu.be/IcdLfajVrZc/)]

## Modules Used
- `requests` – send HTTP requests
- `requests.auth` – handle Basic Authentication

## Output
```
Enter URL (or 'q' to quit): https://httpbin.org/bearer

------------------------------
Requested URL: https://httpbin.org/bearer
{'authenticated': True, 'token': 'Sabir-Hussain-Loser'}
------------------------------


Enter URL (or 'q' to quit): q
Exiting...

Enter URL (or 'q' to quit): https://httpbin.org/basic-auth/user/pass

------------------------------
Requested URL: https://httpbin.org/basic-auth/user/pass
{'authenticated': True, 'user': 'user'}
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
07_authenticated_api_client/
├── main.py
└── README.md
```

## Notes
- Some APIs require authentication, others do not
- If credentials are wrong, API returns error (401/403)
- `httpbin.org` is used for testing authentication
- Never expose real API keys in public code
