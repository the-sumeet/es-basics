A mapping is a way to define schema in ES.
 
ES has reasonable defaults, but sometimes we need to custumize them.

Example, 

```
PUT 127.0.0.1:9200/movies

{
    "mappings": {
        "properties": {
            "year": {
                "type": "date"
            }
        }
    }
}
```

# Common Mappings

Mapping can be used to specify
- Field types
- Field index
- Field analyzer

Field Types:

```
{
    "properties": [
        "user_id": {
            "type": "long"
        }
    ]
}
```

Field Indexing: Whether we want this field to be indexed for full text search or not.

```
{
    "properties": [
        "user_id": {
            "index": "not_analyzed"
        }
    ]
}
```

Field analyzer: define tokenizer and token filter.
```
{
    "properties": [
        "user_id": {
            "analyzer": "english"
        }
    ]
}
```

# Example

```
PUT /movies

{
  "mappings": {
    "properties": {
      "year": {
        "type": "date"
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
  "index": "movies"
}
```

# Example: See the mapping

```
GET /movies/_mapping
```

Output:

```
{
  "movies": {
    "mappings": {
      "properties": {
        "year": {
          "type": "date"
        }
      }
    }
  }
}
```