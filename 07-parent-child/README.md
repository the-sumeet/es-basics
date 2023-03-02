
- We specify the field of type `join`.
- The field has `relations` property.
  - `relations` has key, and value, where `key` represents the `parent`, and the `value` represents the `child/children`.
  - For example, a franchise (parent) can have many films (child).

# Example: Create mapping

```PUT /series
{
  "mappings": {
    "properties": {
      "film_to_franchise": {
        "type": "join",
        "relations": {
          "franchise": "film"
        }
      }
    }
  }
}
```

Output:

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "series"
}
```

# Example: Inserting records

```
PUT /_bulk
{ "create" : { "_index" : "series", "_id" : "1", "routing" : 1} }
{ "id": "1", "film_to_franchise": {"name": "franchise"}, "title" : "Star Wars" }
{ "create" : { "_index" : "series", "_id" : "260", "routing" : 1} }
{ "id": "260", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode IV - A New Hope", "year":"1977" , "genre":["Action", "Adventure", "Sci-Fi"] }
{ "create" : { "_index" : "series", "_id" : "1196", "routing" : 1} }
{ "id": "1196", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode V - The Empire Strikes Back", "year":"1980" , "genre":["Action", "Adventure", "Sci-Fi"] }
{ "create" : { "_index" : "series", "_id" : "1210", "routing" : 1} }
{ "id": "1210", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode VI - Return of the Jedi", "year":"1983" , "genre":["Action", "Adventure", "Sci-Fi"] }
{ "create" : { "_index" : "series", "_id" : "2628", "routing" : 1} }
{ "id": "2628", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode I - The Phantom Menace", "year":"1999" , "genre":["Action", "Adventure", "Sci-Fi"] }
{ "create" : { "_index" : "series",  "_id" : "5378", "routing" : 1} }
{ "id": "5378", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode II - Attack of the Clones", "year":"2002" , "genre":["Action", "Adventure", "Sci-Fi", "IMAX"] }
{ "create" : { "_index" : "series", "_id" : "33493", "routing" : 1} }
{ "id": "33493", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode III - Revenge of the Sith", "year":"2005" , "genre":["Action", "Adventure", "Sci-Fi"] }
{ "create" : { "_index" : "series", "_id" : "122886", "routing" : 1} }
{ "id": "122886", "film_to_franchise": {"name": "film", "parent": "1"}, "title" : "Star Wars: Episode VII - The Force Awakens", "year":"2015" , "genre":["Action", "Adventure", "Fantasy", "Sci-Fi", "IMAX"] }
```

Output:

```
{
  "took": 57,
  "errors": false,
  "items": [
    {
      "create": {
        "_index": "series",
        "_id": "1",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 0,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "series",
        "_id": "260",
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
        "_index": "series",
        "_id": "1196",
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
    },
    {
      "create": {
        "_index": "series",
        "_id": "1210",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 3,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "series",
        "_id": "2628",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 4,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "series",
        "_id": "5378",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 5,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "series",
        "_id": "33493",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 6,
        "_primary_term": 1,
        "status": 201
      }
    },
    {
      "create": {
        "_index": "series",
        "_id": "122886",
        "_version": 1,
        "result": "created",
        "_shards": {
          "total": 2,
          "successful": 1,
          "failed": 0
        },
        "_seq_no": 7,
        "_primary_term": 1,
        "status": 201
      }
    }
  ]
}
```

# Example: Searching for child

```
GET /series/_search
{
  "query": {
    "has_parent": {
      "parent_type": "franchise",
      "query": {
        "match": {
          "title": "star wars"
        }
      }
    }
  }
}
```

Output:

```
{
  "took": 1028,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 7,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "series",
        "_id": "260",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "260",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode IV - A New Hope",
          "year": "1977",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "1196",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "1196",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode V - The Empire Strikes Back",
          "year": "1980",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "1210",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "1210",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode VI - Return of the Jedi",
          "year": "1983",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "2628",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "2628",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode I - The Phantom Menace",
          "year": "1999",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "5378",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "5378",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode II - Attack of the Clones",
          "year": "2002",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi",
            "IMAX"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "33493",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "33493",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode III - Revenge of the Sith",
          "year": "2005",
          "genre": [
            "Action",
            "Adventure",
            "Sci-Fi"
          ]
        }
      },
      {
        "_index": "series",
        "_id": "122886",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "122886",
          "film_to_franchise": {
            "name": "film",
            "parent": "1"
          },
          "title": "Star Wars: Episode VII - The Force Awakens",
          "year": "2015",
          "genre": [
            "Action",
            "Adventure",
            "Fantasy",
            "Sci-Fi",
            "IMAX"
          ]
        }
      }
    ]
  }
}
```

# Example: Searching for parent

```
GET /series/_search
{
  "query": {
    "has_child": {
      "type": "film",
      "query": {
        "match": {
          "title": "The force awakens"
        }
      }
    }
  }
}
```

Output

```
{
  "took": 1,
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
        "_index": "series",
        "_id": "1",
        "_score": 1,
        "_routing": "1",
        "_source": {
          "id": "1",
          "film_to_franchise": {
            "name": "franchise"
          },
          "title": "Star Wars"
        }
      }
    ]
  }
}
```