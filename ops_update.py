import paramiko
import subprocess
import sys
import pexpect
import os




'''
	更新应用所需的先期准备：
		1. 修改TravelServer/settings.py，更改DEBUG为False，添加allowed_hosts
		2. 修改脚本中的 server_ip 和 server_password

'''


server_ip = '118.25.77.165'
server_username = 'root'
server_password = 'smartboys2018'
localpath = '.'
remotepath = '/root/SmartTravelPlan'
uwsgi_ini_path = '/root/SmartTravelPlan/uwsgi.ini'
nginx_conf_path_l = 'TravelServer.conf'
nginx_conf_path_r = '/etc/nginx/conf.d/TravelServer.conf'

trans = paramiko.Transport((server_ip, 22))
trans.connect(username=server_username, password=server_password)
ssh = paramiko.SSHClient()
ssh._transport = trans

sftp = paramiko.SFTPClient.from_transport(trans)
sftp = ssh.open_sftp()

stdin, stdout, stderr = ssh.exec_command('cat /root ' + uwsgi_ini_path)
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('uwsgi --ini ' + uwsgi_ini_path)
print(stdout.read().decode())


trans.close()