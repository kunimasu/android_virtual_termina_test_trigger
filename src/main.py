import os
from typing import Final

import requests

KUNIMASU_URL: Final[str] = os.environ['KUNIMASU_URL']

def main():
    if all([KUNIMASU_URL]):
        post_data = {
            'type': 123
        }
        result: Final[requests.Response] = requests.post(KUNIMASU_URL, json=post_data, headers={"test": "hige"})
        print(str(result.text))
        # print(result.json()["result"])
    else:
        print('Error: app information not configured')

if __name__ == '__main__':
    main()
