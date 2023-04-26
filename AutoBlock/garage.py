#!/usr/bin/python3.6


import socket
import sys
import time
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# for simplicity the variable will simulate a public key, but no public/private
# key pairs are actually used 
PUBLIC_KEY = "GARAGE OFFICIEL MINI"

CAR_DATA_DIR = "car_data"

if not os.path.exists(CAR_DATA_DIR):
    os.makedirs(CAR_DATA_DIR)

def save_car_data(car_id, mileage):
    with open(os.path.join(CAR_DATA_DIR, f"{car_id}.txt"), "w") as f:
        f.write(str(mileage))

def load_car_data(car_id):
    file_path = os.path.join(CAR_DATA_DIR, f"{car_id}.txt")
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        return int(f.read().strip())
    
if len(sys.argv) != 3:
    print("Fournir l'ID d'une voiture!")
    sys.exit(1)

car_id = sys.argv[1]
new_mileage = int(sys.argv[2])

save_car_data(car_id, new_mileage)

block = {
    "timestamp": time.ctime(),
    "car": {
        # there is no check in this demo if a car with this id exists
        # but in the real implementation there would be
        "id": car_id,
        "mileage": new_mileage
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

