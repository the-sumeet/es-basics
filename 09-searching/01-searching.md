We use `GET` for searching, and pass the body for filtering/quering the data.


- Queries returns data in terms of relevance: Wrapped in `query` block.
    - match_all: Default query
    - match: Does analyzed search.
        - `{"match": {"title": "star"}}`
    - multi_match: Runs the same query on multiple fields
        - `{"multi_match": {"query": "star", "fields": ["title", "name"]}}`
    - bool: works like bool filter, but results are scored. Used to combine multiple boolean clauses. Boolean clauses are:
      - filter: Filters ask yes/no questions: Wrapped in `filter` block
        - term
        - terms
        - range
        - exists
        - missing
        - bool
      - must
      - must-not 
      - should

We should use filters when we can, they're faster and cacheble.

We can combine filters in side query, or query inside filters.

### Example

# Getting record with roles = CONSUMER.
# In mapping, roles is defined as keyword, so it will not be analyzed and exact match will be needed.

GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
  "query": {
    "match": {
      "roles": "CONSUMER"
    }
  }
}

### Exampl3

# Using bool query, to combine results of different boolean clauses.
# Let's use range filter to get users with &timestamp > 2010
GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
  "query": {
    "bool": {
      "filter": {
        "range": {
            "&timestamp": {
              "gte": 1262304000000
            }
        }
      }
    }
  }
}

### Example

# Let's use term filter to get users with specific id

GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "&id": "sumeet.mathpati"
        }
      }
    }
  }
}

### Example

Get users having ADMIN role, mfa not activated, and created after or on 1613130426607.

```
GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
    "query": {
        "bool": {
            "must": {
                "match": {
                    "roles": "ADMINISTRATOR"
                }
            },
            "must_not": {
                "match": {
                    "mfaStatus": "ACTIVATED"
                }
            },
            "filter": {
                "range": {
                    "&timestamp": {
                        "gte": 1613130426607
                    }
                }
            }
        }
    }
}
```