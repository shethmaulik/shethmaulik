import paramiko
import time
from getpass import getpass

ip='192.168.50.203'
username = 'admin'
password = 'admin'

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

print ("Connected successfully.")


DEVICE_ACCESS=SESSION.invoke_shell()


DEVICE_ACCESS.send(b'terminal leng 0\n')
time.sleep(1)
DEVICE_ACCESS.send(b'show version\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))



DEVICE_ACCESS.send(b'config terminal\n')
time.sleep(1)
DEVICE_ACCESS.send(b'interface eth0/0\n')
time.sleep(1)
DEVICE_ACCESS.send(b'ip address 192.168.1.1 255.255.255.252\n')
time.sleep(1)
DEVICE_ACCESS.send(b'no shutdown\n')
time.sleep(1)
DEVICE_ACCESS.send(b'end\n')
time.sleep(1)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))


DEVICE_ACCESS.send(b'show ip interface brief\n')
time.sleep(2)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))


SESSION.close
