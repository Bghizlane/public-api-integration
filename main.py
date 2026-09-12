import requests


def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "per_page": 5
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        repositories = response.json()

        print(f"Repositories for {username}:")

        for repository in repositories:
            print("-", repository["name"])

    except requests.RequestException as error:
        print("API request failed.")
        print(error)


get_user_repositories("Bghizlane")