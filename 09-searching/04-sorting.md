# Analyzed strings

A string which is analyzed, can't be used for sorting.

What we can do it, we can create a subtype, and store string as `keyword` there.

For example, this is the mapping for email in `iris_uat_steeleye_co_accountuser`.

This has keywork and text field as well.

```
"email": {
    "type": "keyword",
    "fields": {
        "rfc5322": {
        "type": "text",
        "analyzer": "rfc5322"
        },
        "text": {
        "type": "text",
        "analyzer": "norm"
        }
    },
    "copy_to": [
        "&all"
    ]
}
```

Here we can use `title.raw` for sorting.

# Example

We add field `sort` in request body to do the sorting.

```
GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
    "sort": {
        "email": {
            "order" : "asc"
        }
    }
}
````