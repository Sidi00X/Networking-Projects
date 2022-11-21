import socket

address = input("Server address: ")
port = int(input("Server port"))

def menu():
    print('''\n 0) Close connection
1) Print system info
2) List directory content\n''')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))
print("Connection established")
menu()


while True:

    message = input("Enter message: ")

    if message == "0":
        s.sendall(message.encode())
        s.close()
        break

    elif message == "1":
        s.sendall(message.encode())
        data = s.recv(1024)
        print(data.decode("utf-8"))

    elif message == "2":
        path = input("Enter path: ")
        s.sendall(message.encode())
        s.sendall(path.encode())
        data = s.recv(1024)
        print(data.decode("utf-8"))

    menu()

    
