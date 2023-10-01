# https://www.coursera.org/learn/django-database-web-apps/lecture/alKDL/building-a-simple-web-browser-in-python

#sockets function like files (you can send data and receive it)
import socket

#open the socket (2 step process )
#first you create the socket
#secund make the phone call
#socket.socket means make a phone
#socket.AF_INET means IPv4
#socket.SOCK_STREAM means TCP

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#mysock.connect means dial the phone to a domain name and a port number
mysock.connect(('127.0.0.1', 9000)) #127.0.0.1 is the loopback IP
#to a normal site:
#mysock.connect(('data.pr4e.org', 80))

#send a command
#encode means that we want the data sent in UTF-8
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#to a normal site:
# cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()


#send the command because we are supposed to talk first
mysock.send(cmd)

#retrieving the data

while True:
    #wait until the length is 512
    data = mysock.recv(512)

    #if the socket are closed
    if len(data) < 1:
        break
    #decode convert UTF-8 to unicode
    print(data.decode(),end= "")

mysock.close()