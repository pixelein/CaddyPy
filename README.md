# CaddyPy
#### This app is currently under development
API frontend for caddy api

## Usage
Clone the repo as python package and use

a. Initialize the caddy with your `caddyfile.json` like this example

```
{
  "apps": {
    "http": {
      "servers": {
        "server0": {
          "listen": [
            ":80"
          ],
          "routes": []
        }
      }
    }
  }
}
```

1. Write your caddy config as dict
```
CADDY_CONFIG = {
    "@id": "route1",
    "match": [
        {
            "host": ALLOWED_HOSTS
        }
    ]
    "handle": []     # your handlers
}

```

2. Import and usage
```
from CaddyPy import CaddyApi
caddy_api = CaddyApi()
caddy_api.add_route(data=CADDY_CONFIG, route_id=CADDY_CONFIG["@id"])
```
