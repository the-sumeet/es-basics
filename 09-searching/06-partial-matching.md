# Example: prefix

Get user whose name start with `sum`.

```
GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
    "query": {
        "prefix": {
            "name": "Sum"
        }
}
```

# Example: wildcard

Get user whose name with `mee` in his name.

GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
    "query": {
        "wildcard": {
            "name": "*mee*"
        }
    }
}