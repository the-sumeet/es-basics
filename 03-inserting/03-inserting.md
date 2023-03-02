

# Example

```
PUT /movies/_doc/109487

{
  "genre": ["IMAX", "Sci-Fi"],
  "title": "Interstellar",
  "year": 2014
}
```

Output:

```
{
  "_index": "movies",
  "_id": "109487",
  "_version": 1,
  "result": "created",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1
}
```

# Example: See records

```
GET /movies/_search
```

Output:

```
{
  "took": 474,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "movies",
        "_id": "109487",
        "_score": 1,
        "_source": {
          "genre": [
            "IMAX",
            "Sci-Fi"
          ],
          "title": "Interstellar",
          "year": 2014
        }
      }
    ]
  }
}
```

# Example: Bulk insert

```
PUT /_bulk
{"create": {"_index": "movies", "_id": 135569}}
{"id": 135569, "title": "Star Trek Beyond", "year": 2016, "genre": ["Action", "Adventure", "Sci-Fi"]}
{"create": {"_index": "movies", "_id": 122886}}
{"id": 122886, "title": "Star Wars: Episode VII - The Force Awakens", "year": 2016, "genre": ["Action", "Adventure", "Fantasy", "Sci-Fi", "IMAX"]}
```

Output:

```
{
  "took": 54,
  "errors": false,
  "items": [
    {
      "create": {
        "_index": "movies",
        "_id": "135569",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 1,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "movies",
        "_id": "122886",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 2,
        "_primary_term": 1,
        "status": 201
      }
    }
  ]
}
```