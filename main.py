import requests


def get_github_api():
    url = "https://api.github.com"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("API connection successful.")
        print(data)

    except requests.RequestException as error:
        print("API request failed.")
        print(error)


get_github_api()