import csv
from collections import deque
import elasticsearch
from elasticsearch import helpers

def read_movies():
    csvfile = open("/Users/sumeet/Projects/es-basics/ml-latest-small/movies.csv", "r")

    reader = csv.DictReader(csvfile)
    title_lookup = {}
    
    for movie in reader:
        title_lookup[movie["movieId"]] = movie["title"]
    
    return title_lookup

def readRatings():
    csvfile = open("/Users/sumeet/Projects/es-basics/ml-latest-small/ratings.csv", "r")

    reader = csv.DictReader(csvfile)

    title_lookup = read_movies()

    for line in reader:
        rating = {}
        rating["user_id"] = int(line["userId"])
        rating["movie_id"] = int(line["movieId"])
        rating["title"] = title_lookup[line["movieId"]]
        rating["timestamp"] = int(line["timestamp"])
        rating["rating"] = float(line["rating"])
        yield rating
    
es = elasticsearch.Elasticsearch("http://localhost:9200", verify_certs=False)

es.indices.delete(index="ratings", ignore=404)
deque(helpers.parallel_bulk(es, readRatings(), index="ratings"), maxlen=0)
es.indices.refresh()