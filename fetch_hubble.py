import requests
import json
from fetch_image import fetch_image


def get_extension(path):
    return path.split('.')[-1]


def fetch_image_from_hubble(directory, photo_id):
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(photo_id))
    url = response.json()['image_files'][-1]['file_url']
    fetch_image(directory, 'hubble{}.{}'.format(photo_id, get_extension(url)), url)


def fetch_collection_from_hubble(directory, collection):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection))
    for photo in response.json():
        photo_id = photo['id']
        fetch_image_from_hubble(directory, photo_id)
