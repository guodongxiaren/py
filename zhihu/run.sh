#!/bin/bash
cd `dirname $0`
PATH=$PATH:/usr/local/bin
python zhihu.py >> data.txt
echo "date,voteup,follower" > data.csv
tac data.txt >> data.csv
