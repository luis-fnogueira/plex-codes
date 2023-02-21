# This code locks fields in a plex library

import pandas as pd
from plexapi.server import PlexServer


baseurl = 'http://<your-url>:<your-port>'
token = '<your-token>'
plex = PlexServer(baseurl, token)

# Accessing the library
movies = plex.library.section('<your-section>')

# Locking fields
movies.lockAllField("title")
movies.lockAllField("titleSort")
movies.lockAllField("originalTitle")

