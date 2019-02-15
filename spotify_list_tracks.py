# print all user's saved tracks into a file.txt
# need to create a developper account on spotify developper
# then create an app to get credentials
# and finally to whitelist callback url on the app settings

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'your_login'

clientID = 'your_clientID'
clientSecret = 'your_clientSecret'
redirectURI = 'http://localhost:8888/callback/'  # We/Spotify suggest http://localhost:8888/callback/ or http://localhost/
token = util.prompt_for_user_token(
    username,
    scope,
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirectURI)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    tracks_cleared = []
    filename = 'spotify_tracks.txt'
    f = open(filename,'w')
    while results['next']:
        for item in results['items']:
            track = item['track']
            print >>f, track['name'].encode('utf-8') + ' ' + track['artists'][0]['name'].encode('utf-8')
            # print(track['name'] + ' ' + track['artists'][0]['name'])
        results = sp.next(results)
    f.close()

else:
    print("Can't get token for", username)
