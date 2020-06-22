# Multi-Container Docker Template (Flask, Elasticsearch, Kibana)

Run `build.sh` to spin up the containers using `docker-compose.yml`.

```
./build.sh
```

| URL                     | Service       |
|-------------------------|---------------|
| `http://localhost:9200` | Elasticsearch |
| `http://localhost:5601` | Kibana        |
| `http://localhost:5000` | Flask         |

Within other containers, Elasticsearch is accessed at `http://elasticsearch:9200`.

## Instant Logging

If the Flask application in `/web` uses `stdout` to generate log messages, the output will be captured by Docker instantly due to `PYTHONUNBUFFERED: 0` in `docker-compose.yml`. Running the following will allow you to view these dumped logs.

```
docker-compose logs -f web
```

## Updates on File Change

Bind mounting `/web`, the Flask application directory, to the container in `docker-compose.yml` allows the container to access `/web` on the host file system. When the container starts, it will pick up changes to the mounted code files as they happen and update accordingly.