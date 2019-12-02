#!/bin/bash

# python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python timetable2json.py --help