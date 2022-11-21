import socket

server_addr = input("Server Ip address: ")
server_port = int(input("Server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # AF_INET is the default family socket that uses SOCK_STREAM whick is the default socket which uses TCP.
s.bind((server_addr, server_port))                      # Binds the socket to the provided address and port.
s.listen(1)                             # Listens for incoming connections.
                                        # Number 1 specifies the number of unaccepted connections that the system will allow before refusing new connections. """

print("Server strarted. Waiting for connections ...")
connection, address = s.accept()                            # Connection is the socket object & address is the client address bound to the socket.
print("Client connected with address", address)

while True:
    try:
        data = connection.recv(1024)            # Receives data in the form of bytes from the other socket.
    except: continue
    message = data.decode("utf-8")          # Decodes the received data from octets to letters.

    if message == "1":
        response = platform.platform() + " " + platform.machine()
        connection.sendall(response.encode())               # Encodes the received data from letters to bytes and send it to the other socket.

    elif message == "2":
        path = connection.recv(1024)
        try:
            filelist = os.listdir(path.decode("utf-8"))
            response = ""
            for x in filelist:
                response += "," + x
        except:
            response = "Wrong path"
        connection.sendall(response.encode())

    elif message == "0":
        connection.close()
        connection, address = s.accept() 
        



