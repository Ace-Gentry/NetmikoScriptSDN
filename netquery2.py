import datetime
import os
import netmiko
import paramiko

from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException
from getpass import getpass
from pathlib import Path


username01 = input('Username: ')

password01 = getpass('Enter your password: ')


myCwd = Path.cwd()

backupfile = "csrBackup.txt"

write = "w"

openFile = open(backupfile, write)

routerip = "192.168.108.201"


dict = {"ip" : routerip, "username" : username01, "password" : password01, "device_type" : "cisco_ios"}

try:
    connection = ConnectHandler(**dict)
except (NetMikoTimeoutException):
    print('The following device timed out: ' + dict['ip'])
except (NetMikoAuthenticationException):
    print('Encountered Authentication Error')
except (SSHException):
    print('SSH Error Encountered')

output = connection.send_command('show run')

openFile.write(output)

openFile.close()
