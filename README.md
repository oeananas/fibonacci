## fibonacci
Simple service which calculate fibonacci sequence

## Dependencies
Use redis to caching:

https://redis.io/

Use docker and docker-compose to run application:

https://docs.docker.com/engine/

https://docs.docker.com/compose/install/

## Configuration

By default, the project uses the "production" configuration.
To use the "development" configuration, you need to create a .env file in project root dir with the CONFIGURATION = 'development' parameter.

## Testing

For tests launch you need to to create a .env file in project root dir with the CONFIGURATION = 'base' parameter.
After that you can run tests:
```bash
pytest
```

All project configuration parameters are in config.py file.
```bash
touch .env
echo "CONFIGURATION = 'development'" > .env
```

## Installation

```bash
docker-compose build
docker-compoe run
```

## Usage

Using Python:

```bash
pip install requests
```
```python
import requests

requests.get(
    url='http://localhost/fibonacci',
    params={'from': '1', 'to': '10'}
)
```

Using CURL:
```bash
curl -X GET 'http://localhost/fibonacci?from=3&to=20'
```