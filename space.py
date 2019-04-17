import os
import instabot
import dotenv
from fetch_hubble import fetch_collection_from_hubble
from fetch_spacex import fetch_spacex_last_launch


def post_photos():
    bot = instabot.Bot()
    bot.login(username=os.getenv('login'), password=os.getenv('password'))
    directory = 'images'
    collection = 'spacecraft'
    fetch_spacex_last_launch(directory)
    fetch_collection_from_hubble(directory, collection)
    all_photos = os.listdir(directory)
    for photo in all_photos:
        try:
            bot.upload_photo(os.path.join(directory, photo))
        except RuntimeError:
            continue


if __name__ is '__main__':
    dotenv.load_dotenv()
    post_photos()
