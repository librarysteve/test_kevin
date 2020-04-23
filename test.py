#!/usr/bin/env python
import paramiko
from covid import Covid
import datetime
def put_file(machinename, username,  dirname, passwd, filename, data):
     ssh = paramiko.SSHClient()
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect(machinename,username=username,password=passwd)
     sftp = ssh.open_sftp()
     #try:
     #    sftp.mkdir(dirname)
     #except IOError:
     #    pass
     f = sftp.open(dirname + '/' + filename, 'a+')
     f.write(data)
     f.close()
     ssh.close()

hostname='192.168.71.131'
username='sg'
passwd='badPassword1'
directory='/home/sg/temp'
filename='covid.csv'
covid = Covid()
USA_Cases = covid.get_status_by_country_id(18)
# print(USA_Cases['confirmed'])
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
data =str(yesterday.strftime("%m/%d/%y")) + ',' + str(USA_Cases['confirmed']) + '\n'
put_file(hostname, username, directory, passwd, filename, data)
