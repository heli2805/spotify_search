import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Vos identifiants Spotify
CLIENT_ID = ''
CLIENT_SECRET = ''

# Configuration de l'authentification
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#dictionnaire qui mappe les codes pays aux IDs de playlists correspondantes

country_playlists = {
    'global': '37i9dQZEVXbMDoHDwVN2tF',
    'usa': '37i9dQZEVXbLRQDuF5jeBp',
    'france': '37i9dQZEVXbIPWwFssbupI',
}

#fonction qui récupère les informations pertinentes pour chaque piste dans une playlist.

def get_playlist_tracks(sp, playlist_id, country):
    results = sp.playlist(playlist_id)
    tracks = results['tracks']['items']
    track_list = []
    
    for item in tracks:
        track = item['track']
        track_data = {
            'country': country,
            'added_at': item['added_at'],
            'track_name': track['name'],
            'track_id': track['id'],
            'artist_name': track['artists'][0]['name'],
            'artist_id': track['artists'][0]['id'],
            'album_name': track['album']['name'],
            'album_id': track['album']['id'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'duration_ms': track['duration_ms'],
            'explicit': track['explicit'],
            'external_url': track['external_urls']['spotify']
        }
        track_list.append(track_data)
    
    return track_list

#le dictionnaire des playlists pour récupérer les données pour chaque pays.

all_tracks = []

for country, playlist_id in country_playlists.items():
    tracks = get_playlist_tracks(sp, playlist_id, country)
    all_tracks.extend(tracks)

print(f"Total tracks retrieved: {len(all_tracks)}")

#recupérer les données dans un json 


with open('spotify_top50_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_tracks, f, ensure_ascii=False, indent=4)

