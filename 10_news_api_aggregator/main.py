import requests, json


while True:
    try:
        name = input("\nEnter Topic Name (or 'q' to quit): ").strip()

        if name.lower() == "q":
            print("Exiting...")
            break
        elif not name:
            continue

        url = f"https://hn.algolia.com/api/v1/search?query={name}"



        response = requests.get(url, timeout=5)
        data = response.json()

        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Final Status: {response.status_code}")
        print("\nTop Results:\n")
        for item in data["hits"][:5]:   # only first 5
            title = item.get("title")
            link = item.get("url")

            print(f"Title: {title}")
            print(f"URL: {link}")
            print("-" * 30)
        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")