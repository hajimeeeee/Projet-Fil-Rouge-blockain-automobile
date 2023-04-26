#!/usr/bin/python3.6

import socket
import sys
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# for simplicity the variable will simulate a public key, but no public/private
# key pairs are actually used in this demo
PUBLIC_KEY = "FM-266-DK"

if len(sys.argv) != 3:
    print("Indiquez l'ID de la voiture ainsi que son nouveau kilométrage!")
    print("./maj_kilometrage.py <car_ID> <nouveau_kilometrage>")
    sys.exit(1)

car_id = sys.argv[1]
nouveau_kilometrage = int(sys.argv[2])

block = {
    "timestamp": time.ctime(),
    "car": {
        "id": car_id,
        "mileage": nouveau_kilometrage
    },
    "id": PUBLIC_KEY
}

# send the block to the network
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # in python3 the string must be encoded
    s.sendall(str(block).encode())
    data = s.recv(1024)

print('The block has been received by the network.', repr(data.decode()))
