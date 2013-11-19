from flask import Blueprint, request, jsonify
import app.search.helpers.lastfm as lastfm

mod = Blueprint('search', __name__, url_prefix="/api/v1/search")

@mod.route("/artist=<string:artist>", defaults={"lim":30}, methods=['GET'])
@mod.route("artist=<string:artist>&limit=<int:lim>", methods=['GET'])
def search_by_artist(artist, lim):
    q = lastfm.LastfmSearch(limit=lim)
    data = q.artist(artist)
    return jsonify(data)

@mod.route("/track=<string:track>", defaults={"lim":30}, methods=['GET'])
@mod.route("/track=<string:track>&limit=<int:lim>", methods=['GET'])
def search_by_track(track, lim):
    q = lastfm.LastfmSearch(limit=lim)
    data = q.track(track)
    return jsonify(track)

@mod.route("/artist=<string:artist>&track=<string:track>")
@mod.route("/track=<string:track>&artist=<string:artist>")
def search_by_artist_and_track(artist, track):
    return "Artist: %s Track: %s" % (artist, track)
