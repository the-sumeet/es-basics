
# Analyzer

- Elasticsearch comes with a variety of built-in analyzers that can be used in any index without further configuration. 
- If the built-in analyzers are not suitable for your use case, you can create a custom analyzer. 
- Whether it is a built-in analyzer or a customized analyzer, it is just a package of the three following lower-level building blocks:
    - **Character filter:** Receives the raw text as a stream of characters and can transform the stream by adding, removing, or changing its characters
    - **Tokenizers:** Splits the given streams of characters into a token stream
    - **Token filters:** Receives the token stream and may add, remove, or change tokens

- The standard analyzer is the default analyzer, which is used if none is specified. A standard analyzer consists of the following:
    - Character filter: None
    - Tokenizer: Standard tokenizer
    - Token filters: Lowercase token filter and stop token filter (disabled by default)

## Try Analyzer

```
POST /_analyze
{
  "text": "You will a love Elasticsearch"
}
```

Output is 

```
{
  "tokens": [
    {
      "token": "you",
      "start_offset": 0,
      "end_offset": 3,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "will",
      "start_offset": 4,
      "end_offset": 8,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "a",
      "start_offset": 9,
      "end_offset": 10,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "love",
      "start_offset": 11,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "elasticsearch",
      "start_offset": 16,
      "end_offset": 29,
      "type": "<ALPHANUM>",
      "position": 4
    }
  ]
}
```

Output contains lowercase due to lowercase token filter, and contains stopwords (like 'a') becasue stop token filter is diabled.