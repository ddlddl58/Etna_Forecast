#!/bin/sh

#/usr/bin/python2.7 /home/federica/Scrivania/Research_INGV/Etna_Forecast/get_forecast.py

#cd /home/federica/Scrivania/Research_INGV/Etna_Forecast/hysplit
#python run_forecast.py

DAY=$(date -d "$D" '+%d')
MONTH=$(date -d "$D" '+%m')
YEAR=$(date -d "$D" '+%Y')

#echo "Day: $DAY"
#echo "Month: $MONTH"
#echo "Year: $YEAR"

folder=$DAY$MONTH$YEAR

#echo $folder



GIT=`which git`
REPO_DIR=/home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast/
DATELOG=`date +'%Y-%m-%d-%H-%M-%S'`
LOG="/tmp/${DATELOG}.txt"


cd ${REPO_DIR}
${GIT} add --all .
${GIT} commit -m "Test commit 4"
#export GIT_SSL_NO_VERIFY=1


#${GIT} push --repo https://federicapardini:leobloom1988@bitbucket.org/Etna_Forecast.git >> ${LOG} 2>&1

${GIT} push origin master >> ${LOG} 2>&1
#${GIT} push git@bitbucket.org:federicapardini/Etna_Forecast.git master

#${GIT} push git@bitbucket.org:federicapardini/Etna_Forecast.git master >> ${LOG} 2>&1


#cd /home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast
#git add $folder
#git commit -m "folder added from tha bash script with crontab"
#git push

