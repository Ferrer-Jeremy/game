#!/bin/bash

TC_RESET=$'\x1B[0m'
TC_SKY=$'\x1B[0;37;44m'
CLREOL=$'\x1B[K'
echoHeaderText () {
    echo -n "${TC_SKY}${CLREOL}"
    echo -e "\n           $1${CLREOL}"
    echo -n "${TC_SKY}${CLREOL}"
    echo ${TC_RESET}
}

export COMPOSE_FILE=docker/docker-compose.yml

echoHeaderText '(Re)creating Docker containers'
docker-compose up -d --force-recreate

# For phantomJS/selenium
#docker-compose run --user="www-data" --rm application chmod +x docker/application/geckodriver
#docker-compose run --user="www-data" --rm application xvfb-run &&
#docker-compose run --user="www-data" --rm application bash export DISPLAY=:99


echoHeaderText 'Docker containers'

#chmod u=+x crawl
docker-compose ps
