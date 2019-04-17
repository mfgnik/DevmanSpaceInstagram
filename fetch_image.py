import os
import requests


def fetch_image(directory, filename, url):
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url)
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(response.content)
