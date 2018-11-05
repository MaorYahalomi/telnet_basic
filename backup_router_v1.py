import getpass
import sys
import telnetlib

def connect_to(destinaion):
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    return tn

HOST = "192.168.77.100"
user = "cisco"
password = "cisco"
tel = connect_to(HOST)


tel.write("terminal length 0\n")
tel.write("show run\n")
tel.write("exit\n")
str_all = tel.read_all()

print str_all
#+ means if file not exist then create it!

back = open("C:\Python27\sack3.txt","w+")
back.write(str_all)
back.close()




