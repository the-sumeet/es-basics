import csv
import re
import sys
import pathlib
import requests
import os
from io import StringIO

csvfile = open("/Users/sumeet/Projects/es-basics/ml-latest-small/movies.csv", "r")

reader = csv.DictReader(csvfile)

result = StringIO()
sys.stdout = result


count = 0
for movie in reader:
    
    print("{ \"create\": { \"_index\": \"movies\", \"_id\": \"", movie['movieId'], "\"}}", sep='')
    title = re.sub(" \(.*\)$", "", re.sub('"', '', movie['title']))
    year = movie['title'][-5:-1]
    if (not year.isdigit()):
        year = "2016"
    genres = movie["genres"].split("|")
    print("{ \"id\": \"", movie['movieId'], "\", \"title\": \"", title, "\", \"year\":", year, ", \"genre\": [", end='', sep='')
    for genre in genres[:-1]:
        print("\"", genre, "\",", end="", sep="")
    print("\"", genres[-1], "\"", end="", sep="")
    print("]}")
    count += 1
    if count >= 200:
        break

sys.stdout = sys.__stdout__
result_string = result.getvalue()
r = requests.put("http://127.0.0.1:9200/_bulk", data=result_string, headers={"Content-Type": "application/json"})
