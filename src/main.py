import os
import time
from typing import Final
import requests

KUNIMASU_URL: Final[str] = os.environ['KUNIMASU_URL']
HEAD_SHA: Final[str] = os.environ['HEAD_SHA']
GITHUB_API_URL: Final[str] = os.environ['GITHUB_API_URL']
REPOSITORY: Final[str] = os.environ['REPOSITORY']

def main():
    time.sleep(10)
    if all([KUNIMASU_URL]):
        post_data = {
            'head_sha': HEAD_SHA,
            'github_api_url': GITHUB_API_URL,
            'repository': REPOSITORY
        }
        result: Final[requests.Response] = requests.post(KUNIMASU_URL, json=post_data)
        print(str(result.text))
        # print(result.json()["result"])
    else:
        print('Error: app information not configured')

if __name__ == '__main__':
    main()
