import socket
import sys
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin],[],[])

    for s in inputready:

        if s == my_socket:
            msg = s.recv(1024)
            if msg:
                print msg
            else:
                print "Disconneted from server!"
                running = False

        else:
            line = s.readline()
            my_socket.sendall(line)


# print "reveived:\n%s" % data 


    

my_socket.close()