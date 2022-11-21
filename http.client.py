import http.client

print("*** This program returns a list of methods if OPTIONS is enabled ***\n")

host = input("Enter host IP: ")
port = input("Enter port number (default = 80): ")
url = input("Enter the url: ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("OPTIONS", "/")
    response = connection.getresponse()
    print("Enabled methods are: ", response.getheader("allow"))

except ConnectionRefusedError:
    print("Connection failed")

try:
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Server response: ", response.status)
    connection.close()

except ConnectionRefusedError:
    print("Connection failed")
