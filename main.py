import requests
from openpyxl import Workbook


def get_user_repositories(username):
    # Make a GET request to the GitHub API
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        # If the request was not successful, return None
        return None


def create_excel_of_repositories(username):
    repositories = get_user_repositories(username=username)

    # Create a new workbook
    workbook = Workbook()

    # Get the active sheet (default is the first sheet)
    sheet = workbook.active
    if repositories:
        print(f"Repositories for user {username}:")

        i = 1
        for repo in repositories:
            print(f" - {repo['name']}: {repo['description']}")
            # Add data to the cells
            sheet['a{}'.format(i)] = repo['name']
            sheet['B{}'.format(i)] = repo['description']
            i += 1
        workbook.save(f'{username}_repositories.xlsx')
    else:
        print(f"Failed to fetch repositories for user {username}.")


# Example usage
username = 'mahditavakoli1312'
create_excel_of_repositories(username=username)
