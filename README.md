# Projet : Indexation et Recherche des Données - Spotify Top 50

## Introduction

Ce projet vise à créer un moteur de recherche spécialisé pour analyser l'évolution des hits sur Spotify. L'objectif est de visualiser les tendances musicales mondiales et d'extraire des informations utiles sur les chansons populaires par pays et par semaine.

## Objectifs

- **Collecter** les données des playlists Top 50 de Spotify pour différents pays.
- **Traiter** les données avec Logstash.
- **Stocker** les données traitées dans Elasticsearch.
- **Visualiser** les tendances musicales avec Kibana.
- **Analyser** les données pour extraire des insights pertinents sur la popularité des morceaux et des artistes.

## Technologies Utilisées

- **Spotify API** : Pour récupérer les données musicales.
- **Python** : Pour le scraping des données et l'interaction avec l'API Spotify.
- **Logstash** : Pour le traitement des données avant leur ingestion dans Elasticsearch.
- **Elasticsearch** : Pour le stockage et la recherche des données.
- **Kibana** : Pour la visualisation des données.
- **Docker** : Pour la gestion des conteneurs Elasticsearch, Kibana et Logstash.

## Installation

### Prérequis

- **Python 3.x**
- **Docker** et **Docker Compose** installés sur votre système.

### Étape 1 : Cloner le Répertoire

Clonez ce répertoire sur votre machine locale :

```bash
git clone https://github.com/votre-nom-utilisateur/spotify-top50-analyzer.git
cd spotify-top50-analyzer
```

### Étape 2 : Configurer les Identifiants Spotify

1. Créez un compte développeur sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Créez une nouvelle application pour obtenir votre **Client ID** et **Client Secret**.
3. Modifiez le fichier `spotify_client.py` pour inclure vos identifiants :

```python
CLIENT_ID = 'votre_client_id'
CLIENT_SECRET = 'votre_client_secret'
```

### Étape 3 : Installer les Dépendances Python

Installez les bibliothèques nécessaires avec pip :

```bash
pip install spotipy elasticsearch
```

### Étape 4 : Configurer et Démarrer Elasticsearch, Kibana, et Logstash

1. Créez un fichier `docker-compose.yml` avec le contenu fourni ci-dessous :

```yaml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    container_name: elasticsearch
    environment:
      - node.name=es01
      - cluster.name=es-docker-cluster
      - discovery.type=single-node
      - ELASTIC_PASSWORD=changeme
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata1:/usr/share/elasticsearch/data
    networks:
      - elk

  kibana:
    image: docker.elastic.co/kibana/kibana:8.4.3
    container_name: kibana
    environment:
      - ELASTIC_PASSWORD=changeme
    ports:
      - "5601:5601"
    networks:
      - elk

  logstash:
    image: docker.elastic.co/logstash/logstash:8.4.3
    container_name: logstash
    volumes:
      - ./logstash-config:/usr/share/logstash/config
    networks:
      - elk

volumes:
  esdata1:
    driver: local

networks:
  elk:
    driver: bridge
```

2. Créez un dossier `logstash-config` et ajoutez un fichier `logstash.conf` avec le contenu suivant :

```plaintext
input {
  file {
    path => "/usr/share/logstash/data/spotify_top50_data.json"
    start_position => "beginning"
    codec => "json"
  }
}

filter {
  # Ajoutez des filtres ici si nécessaire
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    index => "spotify-top50"
    user => "elastic"
    password => "changeme"
  }
}
```

3. Démarrez les services avec Docker Compose :

```bash
docker-compose up -d
```

Vérifiez que les services Elasticsearch (port 9200), Kibana (port 5601), et Logstash (port 5044) sont en cours d'exécution.

## Utilisation

### Récupération des Données

1. Exécutez le script Python pour récupérer les données des playlists Top 50 de Spotify :

```bash
python spotify_client.py
```

2. Les données seront sauvegardées dans le fichier `spotify_top50_data.json`.

### Ingestion des Données dans Elasticsearch via Logstash

1. Déplacez le fichier de données dans le répertoire attendu par Logstash :

```bash
cp spotify_top50_data.json logstash-config/
```

2. Logstash ingérera automatiquement les données et les indexera dans Elasticsearch.

### Visualisation des Données avec Kibana

1. Accédez à Kibana via `http://localhost:5601`.
2. Configurez l'index pattern `spotify-top50`.
3. Créez des visualisations pour analyser les données :
   - Artistes les Plus Populaires
   - Top 10 des albums les plus populaire
   - Top 10 des hits les plus écoutés
   - Top 10 des hits les plus écoutés par pays par rapport à la Durée Maximale
   - Répartition des Hits les Plus Écoutés en France par Artiste
   - Top 10 des Artistes les Plus Écoutés en France

## Documentation

- **[API Spotify Documentation](https://developer.spotify.com/documentation/web-api/)**
- **[Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)**
- **[Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)**
- **[Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)**

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue si vous souhaitez proposer des améliorations ou signaler des problèmes.

## Licence

Ce projet est sous la licence de Helicia TSIKA
