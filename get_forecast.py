import urllib 
import datetime
import shutil
import sys
from urllib2 import urlopen


def check (url):
    try:
        u = urlopen(url)
        u.close()
        return True
    except:
        return False

today=datetime.datetime.utcnow()

prevday = datetime.datetime.utcnow()-datetime.timedelta(1)

found = 0

utc=[18,12,06,00]

for i in utc:

    URL = 'ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/hysplit/prod/hysplit.'+str(today.year)+str(today.month).zfill(2)+str(today.day).zfill(2)+'/hysplit.t'+str(i).zfill(2)+'z.gfsf'

    if check(URL):

        print "found : hysplit.t"+str(i).zfill(2)+"z.gfsf"

        urllib.urlretrieve(URL, "hysplit/wind_field.bin")

        found = 1

        break

    else:

        found = 0

if found == 0:

    for i in utc:

        URL = 'ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/hysplit/prod/hysplit.'+str(prevday.year)+str(prevday.month).zfill(2)+str(prevday.day).zfill(2)+'/hysplit.t'+str(i).zfill(2)+'z.gfsf'

        if check(URL):

            print "found : hysplit.t"+str(i).zfill(2)+"z.gfsf"

            urllib.urlretrieve(URL, "hysplit/wind_field.bin")

            found = 1

            break


    

#urllib.urlretrieve('ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/hysplit/prod/hysplit.'+str(today.year)+str(today.month).zfill(2)+str(today.day).zfill(2)+'/hysplit.t00z.gfsf', 'hysplit/wind_field.bin')

#urllib.urlretrieve('ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/hysplit/prod/hysplit.20190402/hysplit.t00z.gfsf', 'hysplit.t00z.gfsf')


