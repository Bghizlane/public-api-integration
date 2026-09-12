import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("User:", data["login"])
        print("Name:", data["name"])
        print("Public repositories:", data["public_repos"])
        print("Followers:", data["followers"])

    except requests.RequestException as error:
        print("API request failed.")
        print(error)


get_github_user("bghizlane")