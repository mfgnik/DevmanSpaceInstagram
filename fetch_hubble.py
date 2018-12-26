import requests
import json
from fetch_image import fetch_image


def get_extension(path):
    return path.split('.')[-1]


def fetch_image_from_hubble(directory, photo_id):
    req = requests.get('http://hubblesite.org/api/v3/image/{}'.format(photo_id))
    url = json.loads(req.text)['image_files'][-1]['file_url']
    fetch_image(directory, 'hubble{}.{}'.format(photo_id, get_extension(url)), url)


def fetch_collection_from_hubble(directory, collection):
    req = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection))
    for photo in json.loads(req.text):
        photo_id = photo['id']
        fetch_image_from_hubble(directory, photo_id)
