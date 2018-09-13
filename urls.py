# coding: utf-8
import os
from config.config import PATH


def app_url():
    apps_url = []
    directory = os.path.join(PATH, 'apps')
    try:
        for filename in os.listdir(directory):
            try:
                full_path = os.path.join(directory, filename)
                if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, 'urls.py')):
                    apps_url += getattr(
                        __import__(os.path.join('apps', filename, 'urls').replace('/', '.'), fromlist=['url']), 'url')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    return apps_url


urls = []
urls += app_url()
