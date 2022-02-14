#!/bin/bash
python3 -m pip install --user virtualenv
python3 -m venv inter
chmod +x get_author.py
. inter/bin/activate
pip install -r requirements.txt
python3 get_author.py #> stdout.txt 2> stderr.txt
