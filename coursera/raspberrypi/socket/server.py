from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(("",8888))

s.listen(5)


while(True):
    conn,addr = s.accept()
    data = conn.recv(1000)
    print('Got request ', data)
    conn.sendall(b"hello client")




