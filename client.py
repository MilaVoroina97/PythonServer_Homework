import socket, threading


# Открываем сокет
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 55555

# Коннектимся

sock.connect((HOST,PORT))

# Подготовим HTTP-запрос
def sock_send():
    data = input('Nick : ').encode('ascii')
    sock.sendall(data)

def sock_recieve():
# Передаём размер буфера - по сколько байт будем перехватывать с нашей сетевой карты приходящих на неё данных и заносить в переменную
    while True:
        data_in = sock.recv(1024)
        print(data_in.decode('ascii'))

sock_send()

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
    data = input()
    if data == '0':
        sock.close()
    sock_send(f"mila: {data}".encode('ascii'))
    sock_send()
