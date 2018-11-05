import getpass
import sys
import telnetlib

HOST = "192.168.77.20"
user = raw_input("Enter your telnet username: ")
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")
tn.write("exit\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()