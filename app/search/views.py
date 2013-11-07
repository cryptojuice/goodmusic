from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for, jsonify
from app.search.helpers.lastfm import LastfmSearch

mod = Blueprint('search', __name__, url_prefix="/1.0/search")

@mod.route("/artist=<string:artist>", defaults={"lim":30}, methods=['GET'])
@mod.route("/artist=<string:artist>&limit=<int:lim>", methods=['GET'])
def search_by_artist(artist, lim):
    q = LastfmSearch(limit=lim)
    data = q.artist(artist)
    return jsonify(data)

@mod.route("/track=<string:track>", defaults={"lim":30}, methods=['GET'])
@mod.route("/track=<string:track>&limit=<int:lim>", methods=['GET'])
def search_by_track(track, lim):
    q = LastfmSearch(limit=lim)
    data = q.track(track)
    return jsonify(track)

@mod.route("/artist=<string:artist>&track=<string:track>")
@mod.route("/track=<string:track>&artist=<string:artist>")
def search_by_artist_and_track(artist, track):
    return "Artist: %s Track: %s" % (artist, track)
