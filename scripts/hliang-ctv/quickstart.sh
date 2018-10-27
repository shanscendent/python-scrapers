#!/bin/bash

# Assumes you have python3 and pip installed
python3 -m venv env
source env/bin/activate
pip install requests bs4 python-qbittorrent
deactivate