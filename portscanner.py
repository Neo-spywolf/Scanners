import pyfiglet
import socket

banner = pyfiglet.figlet_format("WELCOME TO PORT SCANNER")

print(banner)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPv4,TCP

s.settimeout(5)# for speed exxecution

host = input("Enter the Ip address you want to scan: ")#Getting input from user to scan the IPaddresss

port = int(input("Enter the port number you want to scan: "))#getting port number

print("-"*50)
print("Target: ",host)
print("Port: ",port)
print("-"*50)
def port_Scanner(port):
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")

port_Scanner(port)