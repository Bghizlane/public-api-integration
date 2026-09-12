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

        print(f"\nRepositories for {username}:")

        for repository in repositories:
            print(f"- {repository['name']}")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("GitHub user not found.")
        elif response.status_code == 403:
            print("GitHub API rate limit exceeded.")
        else:
            print(f"HTTP error: {response.status_code}")

    except requests.exceptions.RequestException as error:
        print("API request failed.")
        print(error)


username = input("Enter GitHub username: ").strip()

if not username:
    print("Username cannot be empty.")
else:
    get_user_repositories(username)