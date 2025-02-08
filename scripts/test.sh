#!/usr/bin/env -S bash


echo ''
echo '```'
wrk http://127.0.0.1:8000 -d 10 -t 2 -c 200
echo '```'
