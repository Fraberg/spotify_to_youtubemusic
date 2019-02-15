# -*- coding: utf-8 -*-

import sys
from spotify_list_tracks import *
from youtube_search_list import *
from youtube_insert_playlistitem import *
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

if __name__ == '__main__':
    # récupérer les tracks
    fname = 'spotify_tracks.txt'
    with open(fname) as f:
        tracks = f.readlines()
    tracks = [t.strip() for t in tracks]

    # récupérer l'API youtube
    client = get_authenticated_service()

    tracks = tracks[11:20]
    # pour chaque track
    for t in tracks:
        print 'adding ' + t + ' to playlist ...'
        # faire une recherche par pertinence sur Youtube
        t_id = search_list_by_keyword(client, part='snippet', maxResults=1, q=t, type='')
        # ajouter ce track dans une playlist
        playlist_items_insert(client, {
            'snippet.playlistId': 'your_playlistId',
            'snippet.resourceId.kind': 'youtube#video',
            'snippet.resourceId.videoId': t_id,
            'snippet.position': ''
        },
        part='snippet',
        onBehalfOfContentOwner='')
    print "Success"
