- Documents are indexed, stored, and made searchable by using the index API.
- The main purpose of an index is to logically group documents that have certain similar characteristics
- An index is identified by a name (all in lowercase), and this name is referenced in index, search, update, and delete operations for the documents belonging to it.

# Index management APIs

Index management operations allow you to manage the entire life cycle process via its settings, mappings, creation, opening, closing, deletion, and updating indices in an Elasticsearch cluster.

## Index creation: 

The name of the index must follow these requirements:
- Lowercase only
- Cannot include \, /, *, ?, ", <, >, |, spaces, commas, or #
- The colon (:) character can't be used
- Cannot start with -, _, or +
- Cannot be . or ..
- The maximum bytes for the index name is 255

### Example 1

```
PUT /index_name
```

Output:

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "index_name"
}
```

### Example 2

```
PUT /index:name
```

Output:

```
{
  "error": {
    "root_cause": [
      {
        "type": "invalid_index_name_exception",
        "reason": "Invalid index name [index:name], must not contain ':'",
        "index_uuid": "_na_",
        "index": "index:name"
      }
    ],
    "type": "invalid_index_name_exception",
    "reason": "Invalid index name [index:name], must not contain ':'",
    "index_uuid": "_na_",
    "index": "index:name"
  },
  "status": 400
}
```

## Check whether the index exists

### Example 1

```
HEAD /index_name
```

Output:

```
200 - OK
```

## Get the index

This API allows you to retrieve information about one or more indices (for multiple indices).

### Example 1

```
GET /index_name
```

Output:

```
{
  "index_name": {
    "aliases": {},
    "mappings": {},
    "settings": {
      "index": {
        "routing": {
          "allocation": {
            "include": {
              "_tier_preference": "data_content"
            }
          }
        },
        "number_of_shards": "1",
        "provided_name": "index_name",
        "creation_date": "1670776403838",
        "number_of_replicas": "1",
        "uuid": "f7pQ_c4MRQCk6FLPeikrOw",
        "version": {
          "created": "8050399"
        }
      }
    }
  }
}
```

## Deleting Index

### Example 1

```
DELETE /index_name
```

Output:

```
{
  "acknowledged": true
}
```

## Update index

There is no such operation to directly update the contents of the index (that is, PUT/index). 

Instead, you update the mapping of the index, such as PUT/index/_mapping, or update the settings of the index, such as PUT/index/_settings.

# Index Setting

The index settings are divided into per-index level and global level.

Per-index level settings are controlled by index modules. 
- Per-index level settings are also distinguished as static and dynamic. 
0 Static settings can only be set when the index is created or on a closed index, while dynamic settings can be changed on the live index. 

# Index Aliases

The index aliases API allows you to create 
- another name for an index or 
- multiple indices and then use it as an alternative name in an index operation. 

The alias APIs give us flexibility in the following aspects:
- Re-indexing with zero downtime
- Grouping multiple indices
- Views on a subset of documents
