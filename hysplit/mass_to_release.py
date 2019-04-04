import numpy as np
import sys
from haversine import haversine
import os
import datetime

from input_file import *

"""

The routine computes the solid particle loading resulting from the simulation done by PLUME-MoM. This loading is then relased by HYSPLIT

"""

def round_minutes(dt, direction, resolution):

    if ( dt.minute%resolution == 0 ):

        rounded_time = dt

    else: 

        new_minute = (dt.minute // resolution + (1 if direction == 'up' else 0)) * resolution

        rounded_time = dt + datetime.timedelta(minutes=new_minute - dt.minute)

    return rounded_time


time_format = "%y %m %d %H %M"

starttime_hhmm = datetime.datetime.strptime(starttime,time_format)
starttime_round = round_minutes(starttime_hhmm, 'down', 60) # arrotonda per difetto starttime

endemittime_hhmm = datetime.datetime.strptime(endemittime,time_format)
endemittime_round = round_minutes(endemittime_hhmm, 'up', 60) # arrotonda per eccesso endemittime

#print 'starttime',starttime_hhmm,starttime_round
#print 'endemittime',endemittime_hhmm,endemittime_round


runtime=endemittime_round-starttime_round # numero ore arrotondate tra inizio e fine emissione 
n_runs = np.int(np.ceil( runtime.total_seconds() / deltat_plumemom ) ) # numero run di PlumeMoM


solid_mass = []

if n_runs == 1:

    plume_hy = runname + '_{0:03}'.format(1)+'.hy'

    a = np.loadtxt(plume_hy, skiprows = 1)
    a=np.asarray(a)

    timei =  datetime.datetime.strptime(starttime,time_format)
    timei_end =  datetime.datetime.strptime(endemittime,time_format)
    d = datetime.datetime(2000,1,1) + (timei_end-timei)
    duration_mm = str(d.strftime("%M"))
    duration_hh = str(d.strftime("%H"))

  
    solid_mass_partial = sum(sum(a[:,3:]))*(np.float(duration_mm)*60 + np.float(duration_hh)*3600) 
    solid_mass.append([solid_mass_partial])

else:

    for i in range(n_runs):

        plume_hy = runname + '_{0:03}'.format(i+1)+'.hy'
 
        if (i+1) == 1:

            timei =  datetime.datetime.strptime(starttime,time_format)
            timei_end =  starttime_round+datetime.timedelta(seconds=deltat_plumemom)
            d = datetime.datetime(2000,1,1) + (timei_end-timei)
            duration_mm = str(d.strftime("%M"))
            duration_hh = str(d.strftime("%H"))
        

        elif (i+1) == n_runs:


            timei =  starttime_round+datetime.timedelta(seconds=(n_runs-1)*deltat_plumemom)
            endemittime_round = round_minutes(endemittime_hhmm, 'up', 60)
            endemittime_round_down = round_minutes(endemittime_hhmm, 'down', 60)
            timei_end = endemittime_round
            d = datetime.datetime(2000,1,1) + (endemittime_hhmm-timei)
            duration_mm = str(d.strftime("%M"))
            duration_hh = str(d.strftime("%H"))        
   
        else:

            duration_hh = 1        
            duration_mm = 0

        a = np.loadtxt(plume_hy, skiprows = 1)
        a=np.asarray(a)
  
        solid_mass_partial = sum(sum(a[:,3:]))*(np.float(duration_mm)*60 + np.float(duration_hh)*3600) 
        solid_mass.append([solid_mass_partial])

solid_mass = np.asarray(solid_mass)

solid_mass = solid_mass.reshape((-1,1))

print "***------***"

print "--> Solid particle loading from PLUME-MoM: %.1e kg"%(np.sum(solid_mass))
#print "--> Solid particle loading from PLUME-MoM %f kg"%(np.sum(solid_mass))

print " "
#print "    runtime :",runtime," h"

#print "***------***"




"""

The routine computes the gas loading resulting from the simulation done by PLUME-MoM. 

"""


gas_mass = []

if n_runs == 1:

    plume_hy = runname + '_{0:03}_volcgas'.format(1)+'.hy'

    a = np.loadtxt(plume_hy, skiprows = 1)
    a=np.asarray(a)

    timei =  datetime.datetime.strptime(starttime,time_format)
    timei_end =  datetime.datetime.strptime(endemittime,time_format)
    d = datetime.datetime(2000,1,1) + (timei_end-timei)
    duration_mm = str(d.strftime("%M"))
    duration_hh = str(d.strftime("%H"))

  
    gas_mass_partial = sum(sum(a[:,3:]))*(np.float(duration_mm)*60 + np.float(duration_hh)*3600) 
    gas_mass.append([gas_mass_partial])


    for i in range(n_runs):

        plume_hy = runname + '_{0:03}_volcgas'.format(i+1)+'.hy'

 
        if (i+1) == 1:

            timei =  datetime.datetime.strptime(starttime,time_format)
            timei_end =  starttime_round+datetime.timedelta(seconds=deltat_plumemom)
            d = datetime.datetime(2000,1,1) + (timei_end-timei)
            duration_mm = str(d.strftime("%M"))
            duration_hh = str(d.strftime("%H"))
        

        elif (i+1) == n_runs:


            timei =  starttime_round+datetime.timedelta(seconds=(n_runs-1)*deltat_plumemom)
            endemittime_round = round_minutes(endemittime_hhmm, 'up', 60)
            endemittime_round_down = round_minutes(endemittime_hhmm, 'down', 60)
            timei_end = endemittime_round
            d = datetime.datetime(2000,1,1) + (endemittime_hhmm-timei)
            duration_mm = str(d.strftime("%M"))
            duration_hh = str(d.strftime("%H"))        
   
        else:

            duration_hh = 1        
            duration_mm = 0

        a = np.loadtxt(plume_hy, skiprows = 1)
        a=np.asarray(a)
  
        gas_mass_partial = sum(sum(a[:,3:]))*(np.float(duration_mm)*60 + np.float(duration_hh)*3600) 
        gas_mass.append([gas_mass_partial])

gas_mass = np.asarray(gas_mass)

gas_mass = gas_mass.reshape((-1,1))


print "--> Gas loading from PLUME-MoM: %.1e kg"%(np.sum(gas_mass))
#print " "
#print "    runtime :",runtime," h"

print "***------***"


