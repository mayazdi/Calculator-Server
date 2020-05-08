import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))
print(s.recv(4096).decode("utf-8"))
while True:
    inp = input()
    s.send(bytes(inp, "utf-8"))
    if inp == "quit":
        break
    print(s.recv(4096).decode("utf-8"))

s.close()
