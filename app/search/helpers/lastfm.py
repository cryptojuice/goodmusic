from app.config.keys import LASTFM_API_KEY, LASTFM_API_SECRET
import urllib
import json

class LastfmSearch:
    def __init__(self, limit = 30):
        self.BASE_URI = "http://ws.audioscrobbler.com/2.0/?method="
        self.api_key = LASTFM_API_KEY
        self.api_secret = LASTFM_API_SECRET
        self.limit = limit

    def artist(self, artist):
        results = json.loads(urllib.urlopen(self.BASE_URI + \
                "artist.search&artist=%s&api_key=%s&limit=%s&format=json" \
                % (artist, self.api_key, self.limit)).read())
        return results


    def artist(self, track):
        results = json.loads(urllib.urlopen(self.BASE_URI + \
                "track.search&track=%s&api_key=%s&limit=%s&format=json" \
                % (track, self.api_key, self.limit)).read())
        return results
