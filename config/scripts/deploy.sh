#!/bin/sh

# Installing docker engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

cd ~/srv/django-docker/ && docker-compose -f docker-compose.prod.yml up --build -d