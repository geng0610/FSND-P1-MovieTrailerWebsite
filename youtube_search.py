#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from my Google API credentials
DEVELOPER_KEY = "AIzaSyB6Z7KNEpJ85Z6DIztlAqfYuxzJzJ1KKwc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Search for a single trailer clip using a movie name
def trailer_search(movie_name):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified query term.
  search_response = youtube.search().list(
    q=movie_name +' trailer', #attach trailer to the movie name
    part="id,snippet",
    maxResults=1 #only need one result back. anything more and it'd not be useful here
  ).execute()

  # return the youtube link 
  return 'https://youtu.be/'+search_response.get("items", [])[0]["id"]["videoId"]