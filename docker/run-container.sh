#!/usr/bin/env bash
# Abstract the docker-compose run command

docker-compose --file docker/docker-compose.yml run --user="www-data" --rm $*
