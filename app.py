from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
# Configuration d'Elasticsearch
es=Elasticsearch(
    "https://localhost:9200/",
    basic_auth=("elastic","CXY3AQ6jIkLsm7xzG641"),
    verify_certs=False 
)

#Route principale
@app.route('/')
def home():
    return render_template('index.html')



# Route_de_recherche

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    country = request.args.get('country')
    genre = request.args.get('genre')

    # Construire la requête Elasticsearch
    es_query={
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

    """if query:
        es_query['bool']['must'].append({
            "multi_match": {
                "query": query,
                "fields": ["track_name", "artist_name", "album_name"]
            }
        })"""

    """if country:
        es_query['bool']['filter'].append({
            "term": {
                "country.keyword": country
            }
        })

    if genre:
        es_query['bool']['filter'].append({
            "term": {
                "genre.keyword": genre
            }
        })"""

    # Exécuter la recherche
    results = es.search(index="spotify-top50", body={"query": es_query})
    print(results['hits']['hits'])

    # Afficher les résultats
    return render_template('index.html', results=results['hits']['hits'])


if __name__ == '__main__':
    app.run(debug=True)



