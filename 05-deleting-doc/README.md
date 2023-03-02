We use http's `DELETE` method to delete a doc.

# Example

```
DELETE /movies/_doc/135569
```

Output:

```
{
  "_index": "movies",
  "_id": "135569",
  "_version": 2,
  "result": "deleted",
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 5,
  "_primary_term": 1
}
```