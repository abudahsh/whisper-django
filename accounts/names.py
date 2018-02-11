import random
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def generate_nickname():
    """Function generates a nick name by picking a random first name and random second name from 2 separate text files."""
    first=open(os.path.join(BASE_DIR, 'static','first-names.txt'), 'r')
    second=open(os.path.join(BASE_DIR, 'static','middle-names.txt'), 'r')
    nickname=random.choice(first.read().splitlines())+ ' '+random.choice(second.read().splitlines())
    return nickname


def generate_random_pic():
    """Fuction that generate a url for a pic that had a random number as the name of the image.
    \n used to generate random image from the None folder for the whispers that users didn't assign image to.
    """
    return  'whisper_images/None/'+str(random.choice([1,2,3]))+'.jpg'