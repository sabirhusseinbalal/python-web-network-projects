import requests
from requests.auth import HTTPBasicAuth

while True:
    try:
        # Get user input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URL
        if not url.startswith("http"):
            url = f"https://{url}"

        headers = {
            "Authorization": "Bearer Sabir-Hussain-Loser",
            "Content-Type": "application/json"
            }


        # Send GET request with timeout
        # response = requests.get(url, headers=headers, timeout=5)


        response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))



        # Output
        print("\n------------------------------")
        print(f"Requested URL: {url}")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
        print("------------------------------\n")

    # Timeout handling
    except requests.exceptions.Timeout:
        print("Request timed out.")

    # Connection errors, DNS failure, etc.
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    # Any other unforeseen errors
    except Exception as e:
        print(f"Error: {e}")