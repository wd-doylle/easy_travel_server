import paramiko
import subprocess
import sys
import pexpect
import os



'''
	部署应用所需的先期准备：
		1. 修改TravelServer/settings.py，更改DEBUG为False，添加allowed_hosts
		2. 准备TravelServer.conf（用于nginx）和 uwsgi.ini（用于uwsgi）两个配置文件
		3. 修改脚本中的 server_ip 和 server_password

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

sftp.put(localpath, remotepath)
sftp.put(nginx_conf_path_l, nginx_conf_path_r)

stdin, stdout, stderr = ssh.exec_command('yum install python-pip')
stdin.write('y')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('yum install gcc')
stdin.write('y')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('yum install python-devel')
stdin.write('y')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('yum install nginx')
stdin.write('y')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('pip install --upgrade pip setuptools')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('pip install "django<2"')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('pip install uwsgi')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('uwsgi --ini ' + uwsgi_ini_path)
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('nginx')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('firewall-cmd --zone=public --add-port=80/tcp --permanent')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command('firewall-cmd --reload')
print(stdout.read().decode())

stdin, stdout, stderr = ssh.exec_command("sed -i '/^exit 0/i\\nohup %s' /etc/rc.local"%('nginx'))
print stdout.read().decode(),stderr.read().decode()

trans.close()