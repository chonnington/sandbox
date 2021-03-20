# -*- coding: utf-8 -*-
"""
https://github.com/plamere/spotipy
"""

import spotipy
sp = spotipy.Spotify()

results = sp.search(q='Stan Getz', limit=50)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
