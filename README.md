# Public API Integration

A Python project that integrates with the GitHub REST API using the Requests library.

## Features

* Accepts a GitHub username from the user
* Sends HTTP GET requests to the GitHub API
* Retrieves public repositories
* Uses query parameters
* Processes JSON responses
* Handles empty usernames
* Handles HTTP errors such as 404 and 403
* Handles connection and request errors
* Uses a 10-second request timeout

## Technologies

* Python
* Requests
* REST API
* JSON
* Git
* GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/Bghizlane/public-api-integration.git
```

Go to the project directory:

```bash
cd public-api-integration
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Git Bash:

```bash
source venv/Scripts/activate
```

Install Requests:

```bash
pip install requests
```

## Usage

Run the program:

```bash
python main.py
```

Enter a GitHub username when prompted.

Example:

```text
Enter GitHub username: bghizlane

Repositories for bghizlane:
- currency-api
- public-api-integration
- weather-api
```

## Error Handling

The application handles:

* Empty username
* GitHub user not found
* GitHub API rate limits
* Connection errors
* Request errors
* Request timeouts

## Project Structure

```text
public-api-integration/
│
├── main.py
├── README.md
├── .gitignore
└── venv/
```

> The `venv/` directory should not be uploaded to GitHub.

## Author

Bghizlane
