import random
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def generate_nickname():

    first=open(os.path.join(BASE_DIR, 'static','first-names.txt'), 'r')
    second=open(os.path.join(BASE_DIR, 'static','middle-names.txt'), 'r')
    nickname=random.choice(first.read().splitlines())+ ' '+random.choice(second.read().splitlines())
    return nickname

