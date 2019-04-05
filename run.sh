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

#rm -r /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/$folder 

#cd /home/federica/Scrivania/Research_INGV/GIT/Etna_Forecast
#git add $folder
#git commit -m "folder added from tha bash script with crontab"
#git push

echo "***** End *****"

