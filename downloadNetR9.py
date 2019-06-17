from ftplib import FTP
import sys
import ftplib
import os
import fnmatch
import datetime
from datetime import timedelta

today = datetime.date.today()
lusa = today-timedelta(days=2)
kemarin = today-timedelta(days=1)

#tahun = today.strftime('Tahun:%Y')
#bulan = today.strftime('Bulan:%m')
#tanggal = today.strftime('Tanggal:%d')
ftpdirdate= lusa.strftime('/%Y/%m/%d/')
localdirdate=kemarin.strftime('\%y%m_%b')
                                                                                                                         
path= 'Internal/Static'+ftpdirdate 
ftp = ftplib.FTP("192.168.103.108")
ftp.login("admin", "wahyu73")
ftp.cwd(path)
filematch='*T02'
for filename in ftp.nlst(filematch):
    #fhandle=open(filename, 'wb')
    print ('Getting ' + filename)
    local_filename = os.path.join(r"\\SERVERADDRESS\Base_Station_Data_Logging\2018"+localdirdate, kemarin.strftime('NetR9_%Y%m%d_') + filename)
    lf = open(local_filename, "wb")
    ftp.retrbinary('RETR '+ filename, lf.write)
    lf.close()
    
#ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()

print ('Finished')
