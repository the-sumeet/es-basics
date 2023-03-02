A `match` query looks for the existence of a token in a field, whereas a `match_phrase` query looks for the existence of a sequence of tokens (a phrase) in the field.

```
GET /movies/_search
{
  "query": {
    "match_phrase": {
      "title": "star wars",
    }
  }
}
```

# Example

`slop` value is the number of positions of phrases we want to allow in search. For example, if we search for `star beyond` and we want `start trek beyond` to be included, we use slop of `1`.

```
GET /movies/_search
{
  "query": {
    "match_phrase": {
      "title": "star wars",
      "slop": 1
    }
  }
}
```