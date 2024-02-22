import sys
import shelve
import pickle
import os
import math
from utils import helper, textprocessing
from collections import Counter
import json


# Load data from files
db_file = os.path.join(os.getcwd(), 'db', 'index.json')
urls_file = os.path.join(os.getcwd(), 'db', 'urls.json')
lengths_file = os.path.join(os.getcwd(), 'db', 'lengths.json')
stopwords_file = os.path.join(os.getcwd(), 'vietnamese-stopwords-dash.txt')

with open(urls_file, mode='rb') as f:
    urls = json.load(f)
with open(lengths_file, mode='rb') as f:
    lengths = json.load(f)
with open(stopwords_file, mode='r', encoding='utf-8') as f:
    stopwords_set = set(f.read().split())
with open(db_file, mode='rb') as f:
    index_db = json.load(f)

# Get query
query = sys.argv[1]
# Load inverted index

# Construct vocabulary from inverted index
vocabulary = set(index_db.keys())
num_docs = len(urls)

# Preprocess query
tokens = textprocessing.preprocess_text(query, stopwords_set)
tokens = [token for token in tokens if token in vocabulary]

# Caculate weights for query
query_bow = Counter(tokens)

query_weights = {}

for term, freq in query_bow.items():
    df = index_db[term]['df']
    query_weights[term] = helper.idf(df, num_docs) * helper.tf(freq)

# Normalize query weights
query_length = math.sqrt(sum((e ** 2 for e in query_weights.values())))
for term, value in query_weights.items():
    query_weights[term] = value / query_length

# Caculate scores
scores = [[i, 0] for i in range(num_docs)]
for term, query_weight in query_weights.items():
    df = index_db[term]['df']
    postings_list = index_db[term]['postings_list']
    for docId, freq in postings_list.items():
        doc_weight = helper.idf(df, num_docs) * helper.tf(freq)
        docId_int = int(docId)
        scores[docId_int][1] += query_weight * doc_weight / lengths[docId_int]


# Sort scores and display results
scores.sort(key=lambda e: e[1], reverse=True)
for index, score in scores[:20]:
    if score == 0:
        break
    print('{} - {}'.format(urls[index], score))
