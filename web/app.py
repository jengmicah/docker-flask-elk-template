from flask import Flask
from elasticsearch import Elasticsearch
import os

es_host = os.environ['ELASTICSEARCH_URL']
print('Elastic host is {}'.format(es_host))
es = Elasticsearch([es_host])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>My Flask Application</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')