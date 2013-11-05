from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for, jsonify
from app.search.helpers.lastfm import LastfmSearch
import json

mod = Blueprint('search', __name__, url_prefix="/1.0/search")

@mod.route("/artist=<string:artist>")
def search_by_artist(artist):
    q = LastfmSearch(limit=5)
    data = q.artist(artist)
    return jsonify(data)

@mod.route("/track=<string:track>")
def search_by_track(track):
    return "Track: %s" % track

@mod.route("/artist=<string:artist>&track=<string:track>")
@mod.route("/track=<string:track>&artist=<string:artist>")
def search_by_artist_and_track(artist, track):
    return "Artist: %s Track: %s" % (artist, track)
