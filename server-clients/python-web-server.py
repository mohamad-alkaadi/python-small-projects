# https://www.coursera.org/learn/django-database-web-apps/lecture/vNzDJ/building-a-simple-http-server-in-python

from socket import *

def createServer():
    #make a socket (a phone)
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        #I i'm welling to receive a phone call on port 9000
        serverSocket.bind(('localhost', 9000))

        #listen means: Dear operating system, if I'm busy handling one phone call, you can hold on to four more and queue them and then I'll come back and get them for you. (the total is 5)
        serverSocket.listen(5)

        #wait in an infinite loop for incoming request
        while(1):
            #accept means: I'm at the phone, I've registered what my number is and what my extension is, and I'm ready to pick the phone up. Let me know.
            (clientSocket, address) = serverSocket.accept()
            #accept is a blocking meaning the next line never runs until a phone call is received

            #the client talk to us first and we receive the 5000 character request and decode it into unicode
            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")

            #we take the first line and we print it to prove that we got it
            if (len(pieces) > 0):
                print(pieces[0])

            #the response
            data = "HTTP/1.1 200\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello world</body></html>"

            #encode it before you send it to UTF-8 (because the data that is sent inside the socket is UTF-8 )
            clientSocket.sendall(data.encode())

            #after we sent the data we close the connection
            clientSocket.shutdown(SHUT_WR)
            #after the loop is finished go back and wait for a phone call

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serverSocket.close()

print('Access http://localhost:9000')
createServer()

#whatever the request is the response is always hello world