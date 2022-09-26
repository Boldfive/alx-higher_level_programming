#!/usr/bin/python3
"""Python script that takes my github credentials and authenticate to get data."""
import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user', auth=(username, password))
    data = response.json()
    print(data.get('id'))


if __name__ == "__main__":
    main()
