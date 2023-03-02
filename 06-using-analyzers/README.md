Sometimes we want results to be:
- Exact match
- Remotely relevant
    - Resukts can be case-insensitive, stemmed, stopword removed, synonyms applied, etc.
    - Serches with multiple terms need not match them all.
    

# Example

```
GET /movies/_search
{
  "query": {
    "match_phrase": {
      "title": "star wars"
    }
  }
}
```

Even if we've searched for `star wars`, `star trek` also got into the result.
But, the score of `star trek` is lower that the records containing `star wars`.

That's because of the title field is analyzed.

Output:

```
{
  "took": 852,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3,
      "relation": "eq"
    },
    "max_score": 1.1391034,
    "hits": [
      {
        "_index": "movies",
        "_id": "122886",
        "_score": 1.1391034,
        "_source": {
          "id": 122886,
          "title": "Star Wars: Episode VII - The Force Awakens",
          "year": 2016,
          "genre": [
            "Action",
            "Adventure",
            "Fantasy",
            "Sci-Fi",
            "IMAX"
          ]
        }
      },
      {
        "_index": "movies",
        "_id": "1196",
        "_score": 0.65592396,
        "_source": {
          "id": 1196,
          "title": "SStar Wars: Episode V - The Empire Strikes Back",
          "year": 1980,
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "movies",
        "_id": "329",
        "_score": 0.61965394,
        "_source": {
          "id": 329,
          "title": "Star Trek: Generations",
          "year": 1994,
          "genre": [
            "Action",
            "Drama",
            "Sci-Fi"
          ]
        }
      }
    ]
  }
}
```

# Example: exact matching

If we use the following mapping, i.e. use `genre` field as `keyword`, exact matching will be done fot the `genre` while searching.

```
PUT /movies
{
    "mappings": {
        "properties": {
            "id": {
                "type": "integer"
            },
            "year": {
                "type": "date"
            },
            "genre": {
                "type": "keyword"
            },
            "title": {
                "type": "text",
                "analyzer": "english"
            }
        }
    }
}
```

This won't work

```
GET /movies/_search
{
  "query": {
    "match_phrase": {
      "genre": "SciFi"
    }
  }
}
```

This will work

```
GET /movies/_search
{
  "query": {
    "match_phrase": {
      "genre": "Sci-Fi"
    }
  }
}
```

