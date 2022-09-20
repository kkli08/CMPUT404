# CMPUT 404
# Author: Ke Li
# multi_proxy_server.py

import socket, sys
from multiprocessing import Process

# define the buffer size and global address
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# This function is cite from client.py which
# I download from the eclass course page
#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def main():
    host = "www.google.com"
    port = 80

    # This part of the code is cite from echo_server.py which
    # I download from the eclass course page
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)

        # This part of the code is reference on the recording of the lab 2 on eclass page(lab2_Monday.mp4).
        # https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u

        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            p = Process(target=handle_proxy, args=(addr, conn))
            p.daemon = True
            p.start()
            print("started process", p)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_end:
                conn, addr = s.accept()
                print("Connect to Google")
                remote_ip = get_remote_ip(host)

                s_end.connect((remote_ip , port))
                print (f'Socket Connected to {host} on ip {remote_ip}')
        
                # modify start from here
                p = Process(target=handle_proxy, args=(addr, conn))
                p.daemon = True
                p.start()
                print("started process", p)

def handle_proxy(addr, conn):
    #send the data and shutdown
    send_data = conn.recv(BUFFER_SIZE)
    conn.sendall(send_data)
    conn.shutdown(socket.SHUT_WR)

    data = conn.recv(BUFFER_SIZE)
    print("Sending recieved data {data} to client")
    conn.send(data)
    conn.close() 


if __name__ == "__main__":
    main()

# Cite:
# reference the recording lab videos from eclass page
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
# echo_server.py [download from the course web page]
# client.py [download from the course web page]