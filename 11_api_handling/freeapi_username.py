import requests

def fetch_random_username():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()  # ✅ fixed: now calling .json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        totalItems = user_data.get("totalItems", 0)

        # Example: get the first user's country (if available)
        if user_data.get("data"):
            first_user = user_data["data"][0]
            country = first_user.get("location", {}).get("country", "Unknown")
        else:
            country = "N/A"

        return totalItems, country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        totalItems, country = fetch_random_username()
        print(f"Total Users: {totalItems}")
        print(f"First User's Country: {country}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
