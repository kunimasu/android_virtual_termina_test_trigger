import os
import requests
from typing import Final

KUNIMASU_URL: Final[str] = os.environ['KUNIMASU_URL']

def main():
    if all([KUNIMASU_URL]):
        result: Final[requests.Response] = requests.post(KUNIMASU_URL)
        print(str(result.text))
        # print(result.json()["result"])
    else:
        print('Error: app information not configured')


if __name__ == '__main__':
    main()
