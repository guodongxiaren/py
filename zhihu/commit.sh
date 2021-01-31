#!/bin/bash
cd `dirname $0`
PATH=$PATH:/usr/local/bin

git add .
git commit -m"`date +'%Y-%m-%d'`"
git pull --rebase
git push
