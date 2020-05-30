#!/bin/bash
IP=124.64.11.34
curl --header "X-Forwarded-For: $IP" https://www.zhihu.com/api/v4/members/guodongxiaren?include=follower_count%2cvoteup_count > mine.json
exit
python zhihu.py >> data.txt
echo "date,voteup,follower" > data.csv
tac data.txt >> data.csv
