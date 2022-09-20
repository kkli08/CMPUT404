# CMPUT 404
# Author: Ke Li
# proxy_client.py

import socket

# define the buffer size and global address
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

# This part of the code is reference on the recording of the lab 2 on eclass page(lab2_Monday.mp4).
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8001))
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()
# Cite:
# reference the recording lab videos from eclass page
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
# echo_server.py [download from the course web page]
# client.py [download from the course web page]