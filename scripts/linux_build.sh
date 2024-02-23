#!/usr/bin/env bash

echo "Enter root"
su -c 'apt install -y python3-poetry'
poetry install
poetry run build_linux
