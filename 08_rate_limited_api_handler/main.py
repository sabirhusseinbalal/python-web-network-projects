import requests, time

while True:
    try:
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        if not url.startswith("http"):
            url = f"https://{url}"

        tries = 0
        wait = 1

        start_time = time.time()

        while tries < 4:
            response = requests.get(url, timeout=5)
            tries += 1

            if response.status_code == 200:
                break
            elif response.status_code == 429:
                print(f"Rate limited. Retrying in {wait}s...")
                time.sleep(wait)
                wait += 1
            else:
                break

        end_time = time.time() - start_time

        print("\n------------------------------")
        print(f"Requested URL: {url}")
        print(f"Tries: {tries}")
        print(f"Final Status: {response.status_code}")
        print(f"Time Elapsed: {end_time:.2f} seconds")
        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")