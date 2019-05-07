#!/bin/sh

docker-compose exec web python3 manage.py migrate --noinput
docker-compose exec web python3 manage.py migrate --run-syncdb
docker-compose exec web python3 manage.py loaddata datadump_6.json
docker-compose exec web python3 manage.py collectstatic --noinput # && chmod 775 -R /static