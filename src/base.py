import os
import requests
import spotipy


class SongRecommender:
    def __init__(self) -> None:
        self.__entrypoint = "https://accounts.spotify.com/api/token"
        self.__credentials = {
            "grant_type": "client_credentials", 
            "client_id": os.environ["CLIENT_ID"], 
            "client_secret": os.environ["CLIENT_SECRET"]
        }
        authentication = requests.post(self.__entrypoint, self.__credentials).json()["access_token"]
        self.api_client = spotipy.client.Spotify(auth=authentication)
    