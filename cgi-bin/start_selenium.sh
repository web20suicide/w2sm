#!/bin/bash

# read the current id 
#JOBID=444`cat /var/www/tmp/id`
JOBID=$1
#SESSIONID=444`cat /var/www/tmp/session_id`
#firefox -CreateProfile `echo $SESSIONID` --no-remote
#JOBID=$1
#FIREFOXID=`echo /home/killer/.mozilla/firefox/*.${SESSIONID}`
#echo "user_pref("network.proxy.http", "88.212.3.8");user_pref("network.proxy.http_port", 5555);user_pref("network.proxy.type", 1);" >> `echo ${FIREFOXID}/prefs.js`
# start selenium
#java -jar selenium-server.jar -port ${JOBID} -interactive -multiWindow -forcedBrowserMode "*firefox /usr/lib/firefox-3.0.10/firefox" >& /tmp/log${JOBID}
#java -jar selenium-server.jar -port ${JOBID} -interactive -multiWindow -forcedBrowserMode "*firefox /usr/lib/firefox-3.0.10/firefox" -firefoxProfileTemplate "/home/killer/.mozilla/firefox/0pjygtb1.suicide_kiosk"
#java -jar selenium-server1_0_1.jar -port ${JOBID} -Dhttp.proxyHost=localhost -Dhttp.proxyPort=3128 -log /tmp/selenium${JOBID}.log -avoidProxy

java -jar /usr/lib/cgi-bin/selenium-server.jar -port ${JOBID} -interactive -forcedBrowserMode "*firefox /usr/lib/firefox-3.0.10/firefox" -firefoxProfileTemplate "/home/killer/.mozilla/firefox/ze0ym9mm.77777/" -log "/tmp/selenium${JOBID}.log"
#java -jar /usr/lib/cgi-bin/selenium-server.jar -port ${JOBID} -interactive -forcedBrowserMode "*firefox /usr/lib/firefox-3.0.10/firefox"
#java -jar selenium-server.jar -port ${JOBID} -interactive -multiWindow -forcedBrowserMode "*firefox /usr/lib/firefox-3.0.10/firefox" -firefoxProfileTemplate ${FIREFOXID} 
#java -jar selenium-server.jar -port ${JOBID} -interactive -Dhttp.proxyHost=localhost -Dhttp.proxyPort=3128 -multiWindow -log /tmp/selenium${JOBID}.log
