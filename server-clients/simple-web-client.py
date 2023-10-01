# https://www.coursera.org/learn/django-database-web-apps/lecture/vNzDJ/building-a-simple-http-server-in-python

import urllib.request
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

#we get a file handed to us and we loop through
for line in fhand:
    print(line.decode().strip())