from django.conf import settings

import requests


def get_movie_data(title=''):
    res = requests.get(
        settings.OMDB_API_URL,
        params={
            't': title,
            'apikey': settings.OMDB_API_KEY
        }
    )

    if res.status_code == 200:
        return res.json()

    return
