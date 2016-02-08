import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socked created!")

host = 'localhost'
port = 8888

remote_ip = socket.gethostbyname(host)

print("IP Address of " + host + " is " + remote_ip)

s.connect((remote_ip, port))

print("Socket connected to " + host + " on ip " + remote_ip)

message = b"Hello server"
s.sendall(message)

reply = s.recv(1000)

print(reply)

s.close()
