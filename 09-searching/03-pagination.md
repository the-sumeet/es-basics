For pagination, we use `from` and `size`.

`from` start from `0`.

# Example

Get 2 results per page, get first page.

```
GET /movies/_search

{
  "size": 2,
  "from": 0
}
```

Get 2 results [per page, get second page.

```
GET /movies/_search

{
  "size": 2,
  "from": 2
}
```

###

Deep pagination kills performance.

Because if we use `from: 10000`, all the records before that need to be retrieved, collected, and stored.