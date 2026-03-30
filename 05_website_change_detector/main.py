import requests
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

while True:
    try:
        # Input
        url = input("\nEnter URL (or 'q' to quit): ").strip()

        if url.lower() == "q":
            print("Exiting...")
            break
        elif not url:
            continue

        # Fix URL
        if not url.startswith("http"):
            url = f"https://{url}"

        # Create unique file name using hash
        file_name = hashlib.md5(url.encode()).hexdigest()
        file_path = DATA_DIR / f"{file_name}.txt"

        # Send request
        response = requests.get(url, timeout=5)

        # Hash website content
        current_hash = hashlib.md5(response.text.encode()).hexdigest()

        print("\n------------------------------")
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")

        # If file exists → compare
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as f:
                old_hash = f.read()

            if old_hash == current_hash:
                print("No changes detected.")
            else:
                print("Website updated!")
                with file_path.open("w", encoding="utf-8") as f:
                    f.write(current_hash)
        else:
            # First time save
            with file_path.open("w", encoding="utf-8") as f:
                f.write(current_hash)
            print("Website saved for tracking.")

        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        
    except Exception as e:
        print(f"Error: {e}")