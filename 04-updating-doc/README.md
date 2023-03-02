Every document has a `_version` field. 

An ES document is immutable, when we update an existing document, a new document is created with increased version.

The old document is marked for deletion.

We use `POST` request for that.

# Example

Updating multiple fields of a doc.

```
POST /movies/_update/109487
{
  "doc": {
    "year": 2015,
    "title": 1
  }
}
```

Output:

```
{
  "_index": "movies",
  "_id": "109487",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 3,
  "_primary_term": 1
}
```

Now if we see the updated doc, we can see that the version is chagned to `2`.

```
GET /movies/_doc/109487
```

Output:

```
{
  "_index": "movies",
  "_id": "109487",
  "_version": 2,
  "_seq_no": 3,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "genre": [
      "IMAX",
      "Sci-Fi"
    ],
    "title": 1,
    "year": 2015
  }
}
```