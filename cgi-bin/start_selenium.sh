#!/bin/bash

# read the current id 
JOBID=$1

java -jar /usr/lib/cgi-bin/selenium-server1_0_3.jar -port ${JOBID} -interactive -forcedBrowserMode "*firefox /usr/lib/firefox-3.6.3/firefox" -log "/tmp/selenium${JOBID}.log"
