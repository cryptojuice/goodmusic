from app.config.keys import LASTFM_API_KEY, LASTFM_API_SECRET
import json, requests

class LastfmSearch:
    def __init__(self, limit = 1):
        self.BASE_URI = "http://ws.audioscrobbler.com/2.0/?"
        self.api_key = LASTFM_API_KEY
        self.api_secret = LASTFM_API_SECRET
        self.limit = limit

    def artist(self, artist):
        payload = {'artist':artist, 'method':'artist.search', 'format':'json', \
                'limit':self.limit, 'api_key':self.api_key}
        r = requests.get(self.BASE_URI, params=payload)
        return r.json()


    def track(self, track):
        payload = {'track': track, 'method':'track.search', 'format':'json', \
                'limit':self.limit, 'api_key':self.api_key}
        r = requests.get(self.BASE_URI, params=payload)
        return r.json()
