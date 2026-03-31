import requests
from pathlib import Path
from datetime import datetime
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

while True:
    try:
        # Input
        user_input = input("\nEnter City Name (or 'q' to quit): ").strip()

        if user_input.lower() == "q":
            print("Exiting...")
            break
        elif not user_input:
            continue

        # Request
        response = requests.get(f"https://wttr.in/{user_input}?format=j1", timeout=5)

        def flatten_list(data):
            result = {}

            if isinstance(data, dict):
                for key, item in data.items():
                    if isinstance(item, (dict, list)):
                        result.update(flatten_list(item))
                    else:
                        result[key] = item

            elif isinstance(data, list):
                for item in data:
                    result.update(flatten_list(item))

            return result

        # Extract data
        data = flatten_list(response.json())

        data_list = ["temp_C", "humidity"]

        results = {
            "city": user_input,
            "date": str(datetime.today().date())
        }

        for key in data_list:
            results[key] = data.get(key, "N/A")

        # Convert to DataFrame (FIX: wrap in list)
        df = pd.DataFrame([results])

        csv_path = DATA_DIR / "data.csv"

        # If file exists → append
        if csv_path.exists():
            old_df = pd.read_csv(csv_path)
            df = pd.concat([old_df, df], ignore_index=True)

        # Save
        df.to_csv(csv_path, index=False)

        print("\n------------------------------")
        print(f"City: {user_input}")
        print(f"Results: {results}")
        print(f"Saved to: {csv_path}")
        print("------------------------------\n")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    except Exception as e:
        print(f"Error: {e}")