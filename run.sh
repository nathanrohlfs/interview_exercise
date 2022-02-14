#!/bin/bash
. inter/bin/activate
python3 get_author.py #> stdout.txt 2> stderr.txt
