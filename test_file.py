import socket
import sys
import select

def open_connection(host, port):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, port))
    return my_socket


def format_message(inputready, my_socket):
    for s in inputready:

        if s == my_socket:
            msg = s.recv(1024)
            if msg:
                print msg
                return True
            else:
                print "Disconneted from server!"
                return False

        else:
            line = s.readline()
            my_socket.sendall(line)
            return True



def main():
    my_socket = open_connection('10.1.10.100', 5555)
    running = True
    while running:
        inputready, outputready, exceptready = select.select([my_socket, sys.stdin],[],[])

        running = format_message(inputready, my_socket)

    my_socket.close()

main()

