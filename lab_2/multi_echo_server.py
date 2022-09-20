import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

# the code in main function is cited from echo_server.py
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            p = Process(target=handle_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("started process", p)
        
# This part of the code is reference on the recording of the lab 2 on eclass page(lab2_Monday.mp4).
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
def handle_echo(addr, conn):
    print("print by ", addr)
    #recieve data, wait a bit, then send it back
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()

# Cite:
# reference the recording lab videos from eclass page
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
# echo_server.py [download from the course web page]
# client.py [download from the course web page]