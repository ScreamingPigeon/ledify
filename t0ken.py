import spotipy
from secrets import clientId, clientSecret, redirectUri
from spotipy.oauth2 import SpotifyOAuth


scopes = "user-read-playback state user-modify-playback-state user-read-currently-playing app-remote-control playlist-read-private user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scopes, client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUri))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
