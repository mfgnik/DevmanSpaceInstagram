import os
import requests


def fetch_image(directory, filename, url):
    if not os.path.exists(directory):
        os.makedirs(directory)
    req = requests.get(url)
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(req.content)
