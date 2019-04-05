import subprocess
import datetime
import os

from datetime import datetime, timedelta

subprocess.call("/usr/bin/python2.7 /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/clean_all.py", shell = True)

today=datetime.utcnow()

runname = today.strftime("%d%m%Y_%H")

starttime=today.strftime("%Y %m %d %H")[2:]

endemittime=(datetime.today()+timedelta(hours=6)).strftime("%Y %m %d %H")[2:]

endruntime=(datetime.today()+timedelta(hours=6)).strftime("%Y %m %d %H")[2:]

f = open('input_file.template','r')
filedata = f.read()
f.close()

filedata = filedata.replace("{runname}", str(runname) )
filedata = filedata.replace("{starttime}", str(starttime)+" 00" )
filedata = filedata.replace("{endemittime}", str(endemittime)+" 00" )
filedata = filedata.replace("{endruntime}", str(endruntime)+" 00" )

f = open('input_file.py','w')
f.write(filedata)
f.close()

subprocess.call("/bin/sh /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/run_plumemom_hysplit.sh", shell = True)
subprocess.call("/bin/sh /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/create_plots.sh", shell = True)

plot_dir=today.strftime("%d%m%Y")




if os.path.exists("/home/utente/Scrivania/Codes/Etna_Forecast/hysplit/"+str(plot_dir)):
    subprocess.call("rm -r /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/"+str(plot_dir), shell=True)
    os.mkdir("/home/utente/Scrivania/Codes/Etna_Forecast/hysplit/"+str(plot_dir))
else:
    os.mkdir("/home/utente/Scrivania/Codes/Etna_Forecast/hysplit/"+str(plot_dir))


subprocess.call("cp /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/*.pdf "+str(plot_dir), shell = True)

#subprocess.call("/usr/bin/python2.7 /home/utente/Scrivania/Codes/Etna_Forecast/hysplit/clean_all.py", shell = True)





