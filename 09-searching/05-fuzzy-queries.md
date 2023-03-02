Fuzzy queries are way to account for typos and missspellings.

The Levinshtein distance accounts for:
- Substitution of characters
- Insertion of characters
- Deletion of character

# Auto Fuziness

The default fuzziness value will tolerate following number of fuzzy chars depending on length of the string

`0` chars for `1-2` string length.
`1` chars for `3-5` string length.
`2` chars for string length more than 5.

# Example

```
GET http://127.0.0.1:9200/iris_uat_steeleye_co_accountuser/_search

{
    "query": {
        "fuzzy": {
            "&id": {
                "value": "tvmeet.mathpati",
                "fuzziness": 2
            }
        }
    }
}
```

