
Flattened fields will be treated as keywords, hence, no analyzers and tokenizers will be applied while searching.

# Example: Create mapping

```
PUT /demo-flattened/_mapping
{
  "properties": {
    "host": {
      "type": "flattened"
    }
  }
}
```

# Example: Add data

```
PUT /demo-flattened/_doc/1
{
  "message": "[5592:1:0309/123054.737712:ERROR:child_process_sandbox_support_impl_linux.cc(79)] FontService unique font name matching request did not receive a response.",
  "fileset": {
    "name": "syslog"
  },
  "process": {
    "name": "org.gnome.Shell.desktop",
    "pid": 3383
  },
  "@timestamp": "2020-03-09T18:00:54.000+05:30",
  "host": {
    "hostname": "bionic",
    "name": "bionic"
  }
}
```

# Example: See mapping

```
GET /demo-flattened/_mapping
```

Output:

Fields inside the `host` are not mapped after insertion, while the fields inside the `fileset`, `process`, etc got mapping.

```
{
  "demo-flattened": {
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "fileset": {
          "properties": {
            "name": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "host": {
          "type": "flattened"
        },
        "message": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "process": {
          "properties": {
            "name": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "pid": {
              "type": "long"
            }
          }
        }
      }
    }
  }
}
```