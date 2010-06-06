#!/bin/bash

# read the current id 
#JOBID=`cat /var/www/tmp/id`
JOBID=$1
USER=killer
HOME=/home/killer
export USER HOME

vncserver :${JOBID} -depth 16 
