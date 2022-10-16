import os
from typing import Final

import requests

KUNIMASU_URL: Final[str] = os.environ['KUNIMASU_URL']
REPO_NAME: Final[str] = os.environ['REPO_NAME']
REPO_OWNER: Final[str] = os.environ['REPO_OWNER']

def main():
    if all([KUNIMASU_URL]):
        post_data = {
            'type': 123
        }
        result: Final[requests.Response] = requests.post(KUNIMASU_URL, json=post_data, headers={"test": "123"})
        print(str(result.text), REPO_NAME, REPO_OWNER, "end")
        # print(result.json()["result"])
    else:
        print('Error: app information not configured')

if __name__ == '__main__':
    main()
