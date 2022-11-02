import os
import time
from typing import Final
import requests

KUNIMASU_URL: Final[str] = os.environ['KUNIMASU_URL']
GITHUB_TOKEN: Final[str] = os.environ['GITHUB_TOKEN']
REPO_NAME: Final[str] = os.environ['REPO_NAME']
REPO_OWNER: Final[str] = os.environ['REPO_OWNER']
REPO_HEAD_SHA: Final[str] = os.environ['REPO_HEAD_SHA']

def main():
    time.sleep(10)
    if all([KUNIMASU_URL]):
        post_data = {
            'github_token': GITHUB_TOKEN,
            'repo_name': REPO_NAME,
            'repo_owner': REPO_OWNER,
            'repo_head_sha': REPO_HEAD_SHA
        }
        result: Final[requests.Response] = requests.post(KUNIMASU_URL, json=post_data)
        print(str(result.text), REPO_NAME, REPO_OWNER, REPO_HEAD_SHA, GITHUB_TOKEN, "end")
        # print(result.json()["result"])
    else:
        print('Error: app information not configured')

if __name__ == '__main__':
    main()
