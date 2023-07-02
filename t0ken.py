from PIL import Image
import urllib.request
import spotipy
import time
import os
import threading
from spotipy.oauth2 import SpotifyOAuth
from secrets import clientId, clientSecret, redirectUri


scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control playlist-read-private user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes, client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUri))
old_name = ''

 
def getDevice():
    for device in spotify.devices()['devices']:
        if device['is_active'] == True:
            return(device)
    return None

def nextTrack(device):#needs spotify premium
    spotify.next_track(device['id'])

def prevTrack(device):#needs spotify premium
    spotify.previous_track(device['id'])

def playPause(device):#needs spotify premium
    spotify.pause_playback(device['id'])



while True:
    try:
        active_device = getDevice()
        if active_device is None:
            Exception('No active device')#causes loop to wait 5s before checking for new device
        results = spotify.current_user_playing_track()  # fetches data from spotify api
        # gets album cover image url from response
        img_url = results['item']['album']['images'][0]['url']
        # gets album name from response
        album_name = results['item']['album']['name']
        if album_name != old_name:
            old_name = album_name
            fullpath = 'album_covers/' + album_name + \
                '.jpeg'  # sets path in album_covers folder
            if not os.path.isfile(fullpath):  # checks if album cover already saved
                # downloads and saves image in album_covers folder
                urllib.request.urlretrieve(img_url, fullpath)
            img = Image.open(fullpath)
            img.show()
            time.sleep(0.5)
    except:
        time.sleep(5)


