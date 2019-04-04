#!/bin/sh

echo "***** Start *****"

cd /home/utente/Scrivania/Codes/Etna_Forecast

/usr/bin/python2.7 /home/utente/Scrivania/Codes/Etna_Forecast/get_forecast.py

cd /home/utente/Scrivania/Codes/Etna_Forecast/hysplit

python run_forecast.py

DAY=$(date -d "$D" '+%d')
MONTH=$(date -d "$D" '+%m')
YEAR=$(date -d "$D" '+%Y')

folder=$DAY$MONTH$YEAR

/home/utente/dropbox_uploader.sh upload /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/$folder Etna_Forecast 

#cd /home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast
#git add $folder
#git commit -m "folder added from tha bash script with crontab"
#git push

echo "***** End *****"

#rm -r $folder

#echo $folder



#GIT=`which git`
#REPO_DIR=/home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast/
#DATELOG=`date +'%Y-%m-%d-%H-%M-%S'`
#LOG="/tmp/${DATELOG}.txt"


#cd ${REPO_DIR}
#${GIT} add --all .
#${GIT} commit -m "Test commit 3"

#/usr/bin/git add --all
#/usr/bin/git commit -am 'automated weekly update 4'
#/usr/bin/git push -u origin master
#/usr/bin/git push https://federicapardini:leobloom1988@github.com/federicapardini/Etna_Forecast.git master ${LOG} 2>&1

#export GIT_SSL_NO_VERIFY=1


#${GIT} push --repo https://federicapardini:leobloom1988@bitbucket.org/Etna_Forecast.git >> ${LOG} 2>&1

#${GIT} push origin master >> ${LOG} 2>&1
#${GIT} push git@bitbucket.org:federicapardini/Etna_Forecast.git master

#${GIT} push git@bitbucket.org:federicapardini/Etna_Forecast.git master >> ${LOG} 2>&1


#cd /home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast
#git add $folder
#git commit -m "folder added from tha bash script with crontab"
#git push

