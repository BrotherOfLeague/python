#!/bin/bash
while : 
    do setsid python CSDNGrade.py 
    sleep 3600
    killall -9 python
done


