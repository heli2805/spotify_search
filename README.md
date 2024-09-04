# 🎵 **Projet : Indexation et Recherche des Données - Spotify Top 50**

## 🎯 **Introduction**

Ce projet vise à créer un moteur de recherche spécialisé pour analyser l'évolution des hits sur Spotify. L'objectif est de visualiser les tendances des hits en france , USA et globale

## 📝 **Objectifs**

- **Collecter** les données des playlists Top 50 de Spotify.
- **Stocker** les données traitées dans Elasticsearch.
- **Visualiser** les tendances musicales avec Kibana.
- **Analyser** les données pour extraire des insights pertinents sur la popularité des morceaux et des artistes.
- **Développer** une application Flask pour rechercher et visualiser les données.

## 💻 **Technologies Utilisées**

- **🎧 Spotify API** : Pour récupérer les données musicales.
- **🐍 Python** : Pour le scraping des données et l'interaction avec l'API Spotify.
- **🔍 Elasticsearch** : Pour le stockage et la recherche des données.
- **📊 Kibana** : Pour la visualisation des données.
- **🐳 Docker** : Pour la gestion des conteneurs Elasticsearch et Kibana.
- **🌐 Flask** : Pour développer l'application web de recherche.

## ⚙️ **Installation**

### 📋 **Prérequis**

- **Python 3.x**
- **Docker** et **Docker Compose** installés sur votre système.

### 🚀 **Étape 1 : Cloner le Répertoire**

Clonez ce répertoire sur votre machine locale :

```bash
git clone https://github.com/votre-nom-utilisateur/spotify-top50-analyzer.git
cd spotify-top50-analyzer
```

### 🔑 **Étape 2 : Configurer les Identifiants Spotify**

1. Créez un compte développeur sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Créez une nouvelle application pour obtenir votre **Client ID** et **Client Secret**.
3. Modifiez le fichier `spotify_client.py` pour inclure vos identifiants :

```python
CLIENT_ID = 'votre_client_id'
CLIENT_SECRET = 'votre_client_secret'
```

### 📦 **Étape 3 : Installer les Dépendances Python**

Installez les bibliothèques nécessaires avec pip :

```bash
pip install spotipy elasticsearch flask
```

### 🐳 **Étape 4 : Configurer et Démarrer Elasticsearch et Kibana**

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

volumes:
  esdata1:
    driver: local

networks:
  elk:
    driver: bridge
```

2. Démarrez les services avec Docker Compose :

```bash
docker-compose up -d
```

Vérifiez que les services Elasticsearch (port 9200) et Kibana (port 5601) sont en cours d'exécution.

### ⚡ **Étape 5 : Lancer l'Application Flask**

1. Lancez l'application Flask pour démarrer le moteur de recherche :

```bash
python app.py
```

2. Accédez à l'application via `http://localhost:5000`.

## 🚀 **Utilisation**

### 📥 **Récupération des Données**

1. Exécutez le script Python pour récupérer les données des playlists Top 50 de Spotify :

```bash
python spotify_client.py
```

2. Les données seront automatiquement indexées dans Elasticsearch.

### 🔍 **Recherche et Visualisation des Données**

1. Accédez à l'application Flask pour effectuer des recherches sur les chansons, artistes, et albums.
2. Visualisez les tendances musicales à l'aide du tableau de bord Kibana via `http://localhost:5601`.

## 📚 **Documentation**

- **[API Spotify Documentation](https://developer.spotify.com/documentation/web-api/)**
- **[Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)**
- **[Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)**
- **[Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)**

## 🤝 **Contribuer**

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue si vous souhaitez proposer des améliorations ou signaler des problèmes.

## 📝 **Licence**

Ce projet est sous la licence de Helicia TSIKA.
