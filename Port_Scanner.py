import socket

target = input("Enter target address: ")
port_range = input("Enter port range (x-y): ")

lowport = int(port_range.split("-")[0])
highport = int(port_range.split("-")[1])

print("Scanning target", target, "from port", lowport, "to", highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print("*** Port", port, " OPENED ***")
    else:
        print("Port", port, "closed")

s.close()
