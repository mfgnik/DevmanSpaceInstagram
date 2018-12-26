import requests
import json
from fetch_image import fetch_image


def get_photos_links_of_last_launch_from_spacex():
    req = requests.get('https://api.spacexdata.com/v3/launches/past')
    launches_list = json.loads(req.text)
    number_of_launch = 0
    while not launches_list[number_of_launch]['links']['flickr_images']:
        number_of_launch += 1
    return launches_list[number_of_launch]['links']['flickr_images']


def fetch_spacex_last_launch(directory):
    for number_of_photo, photo in enumerate(get_photos_links_of_last_launch_from_spacex(), 1):
        filename = 'spacex{}.jpg'.format(number_of_photo)
        fetch_image(directory, filename, photo)
