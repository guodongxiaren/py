#!/bin/bash
python zhihu.py >> data.txt
echo "date,voteup,follower" > data.csv
tac data.txt >> data.csv
