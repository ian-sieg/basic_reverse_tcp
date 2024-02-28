import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

sock.bind((HOST, PORT))
print ("Listening...")
sock.listen()

conn, addr = sock.accept()

print("Accepted incoming connection from:", addr)

while True:
    command = input('Enter a command >> ')
    
    if command == 'exit':
        break
    
    conn.send(command.encode())
    
    msg = conn.recv(8096).decode()
    print(msg)

print("Connection closed")
conn.close()