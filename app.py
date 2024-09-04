from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Configuration d'Elasticsearch
es = Elasticsearch(
    "https://localhost:9200/",
    basic_auth=("elastic", "CXY3AQ6jIkLsm7xzG641"),
    verify_certs=False
)

# Route principale
@app.route('/')
def home():
    return render_template('index.html')

# Route de recherche
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    
    if query:
        # Construire la requête Elasticsearch
        es_query = {
            "multi_match": {
                "query": f"{query}",
                "fields": [
                    "country",
                    "artist",
                    "artist_name",
                    "album_name",
                    "track_name"
                ]
            }
        }

        # Exécuter la recherche
        results = es.search(index="spotify-top50", body={"query": es_query})

        # Passer les résultats et la requête au template
        return render_template('index.html', results=results['hits']['hits'], query=query)
    else:
        # Passer une requête vide au template si aucune requête n'est fournie
        return render_template('index.html', query=None)

if __name__ == '__main__':
    app.run(debug=True)
