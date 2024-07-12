#!/bin/bash

while true
do
    random_ip=$(dd if=/dev/urandom bs=4 count=1 2>/dev/null | od -An -tu1 | sed -e 's/^ *//' -e 's/  */./g')
    random_size=$(( (RANDOM % 65535) + 1 ))

    current_date_time=$(date '+%d/%b/%Y:%H:%M:%S %z')

    echo "$random_ip - - [$current_date_time] INFO \"GET /data.php HTTP/1.1\" 200 $random_size" | tee -a 'random_log'
    echo "$random_ip - - [$current_date_time] ERROR \"unable to resolve dns redis.internal\" 500 $random_size" | tee -a 'random_log'

    sleep $(( ( RANDOM % 10 )  + 2 ))
done