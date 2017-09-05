#!/usr/bin/env bash

read -r -p "Are you sure? [y/N] " response
if [[ "$response" =~ ^(yes|y)$ ]]
then
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker rmi $(docker ps -a -q)
    docker volume rm $(docker volume ls -qf dangling=true)
    docker network rm $(docker network ls -q)
fi
