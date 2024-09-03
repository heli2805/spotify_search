import json
from elasticsearch import Elasticsearch, helpers
from Projet_elasticsearch.scripts.spotify_client import sp, get_playlist_tracks, country_playlists
import urllib3


# Désactiver les avertissements pour les requêtes non sécurisées
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration d'Elasticsearch
es=Elasticsearch(
    "https://localhost:9200/",
    basic_auth=("elastic","CXY3AQ6jIkLsm7xzG641"),
    verify_certs=False 
)

# Nom de l'index dans Elasticsearch
index_name = 'spotify-top50'

# Récupération des données depuis Spotify
all_tracks = []
for country, playlist_id in country_playlists.items():
    tracks = get_playlist_tracks(sp, playlist_id, country)
    all_tracks.extend(tracks)

print(f"Total tracks retrieved: {len(all_tracks)}")

# Sauvegarder les données dans un fichier JSON (optionnel)
with open('spotify_top50_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_tracks, f, ensure_ascii=False, indent=4)

# Préparation des actions pour l'ingestion dans Elasticsearch
actions = [
    {
        "_index": index_name,
        "_source": track,
    }
    for track in all_tracks
]

# Création de l'index si nécessaire
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Ingestion des données dans Elasticsearch
helpers.bulk(es, actions)

print(f"Total tracks indexed in Elasticsearch: {len(all_tracks)}")
