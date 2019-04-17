import requests
import json
from fetch_image import fetch_image


def get_photos_links_of_last_launch_from_spacex():
    response = requests.get('https://api.spacexdata.com/v3/launches/past')
    launches_list = response.json()
    for launch in launches_list:
        if launch['links']['flickr_images']:
            return launch


def fetch_spacex_last_launch(directory):
    for number_of_photo, photo in enumerate(get_photos_links_of_last_launch_from_spacex(), 1):
        filename = 'spacex{}.jpg'.format(number_of_photo)
        fetch_image(directory, filename, photo)
