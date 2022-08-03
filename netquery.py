import datetime
import os
import netmiko

from netmiko import ConnectHandler
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

connection = ConnectHandler(**dict)

output = connection.send_command('show run')

date = datetime.datetime.now()

openFile.write(output)

openFile.close()

