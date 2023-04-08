import socket
import threading

# создаем серверный сокет:

serv_sock = socket.socket(socket.AF_INET,     #задаем семейство протоколов "Интернет" (INET)
                          socket.SOCK_STREAM, #задаем тип передачи данных "потоковый" (TCP)
                          proto=0             #выбираем протокол по умолчанию для TCP, т.е. IP
                          )

# print(type(serv_sock))

HOST = '127.0.0.1'
PORT = 55555
hosts = []#создаем отдельный список хостов-клиентов
names = []#и их имена

serv_sock.bind((HOST,PORT))# привязываем созданные сокет к сетевому адаптеру
# backlog = 10#Размер очереди входящих подключений
serv_sock.listen()

# Функция установления соединения с клиентами и получение сообщений от них:

def server_receive():
    while True:
        client_sock,client_addr = serv_sock.accept()
        print("Connected to {}".format(str(client_addr)))
        client_sock.send('Nickname: '.encode('ascii'))
        NICK = client_sock.recv(1024).decode('ascii')
        print("Nickname is {}".format(NICK))
        names.append(NICK)
        hosts.append(client_sock)
        send_to_all("{} is here".format(NICK).encode('ascii'))
        client_sock.send('Connected to server'.encode('ascii'))
        thread = threading.Thread(target=get_message,args=(client_sock,))
        thread.start()

# Функиция для отправки сообщения всем хостам:

def send_to_all(data):
    for host in hosts:
        host.send(data)

# Функиция для получения сообщения сервером от хоста:

def get_message(host):
    while True:
        data = host.recv(1024)
        send_to_all(data)

server_receive()
