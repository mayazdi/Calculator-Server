import socket
import math

def parse_data(data):
    
    try:
        li = data[:-2].split("$ ")
        print("----------")
        print(li)
        print("----------")
        cmd = li[1][:-1]
        if cmd.lower()=="add":
            return str(int(li[2][:-1]) + int(li[3]))
        elif cmd.lower()=="subtract":
            return str(int(li[2][:-1]) - int(li[3]))
        elif cmd.lower()=="divide":
            return str(int(li[2][:-1]) / int(li[3]))
        elif cmd.lower()=="multiply":
            return str(int(li[2][:-1]) * int(li[3]))
        elif cmd.lower()=="sin":
            return str(math.sin(int(li[2])))
        elif cmd.lower()=="cos":
            return str(math.cos(int(li[2])))
        elif cmd.lower()=="tan":
            return str(math.tan(int(li[2])))
        elif cmd.lower()=="cot":
            return str(math.tan(1 / int(li[2])))
        else:
            return "Non Parsable Here"
    except:
            return "Non Parsable there"



serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)

conn, addr = serv.accept()
from_client = ''

conn.send(bytes("You are connected to the server!", "utf-8"))

while True:
    data = conn.recv(4096).decode("utf-8")
    if data == "quit":
        break
    retVal = parse_data(data)
    conn.send(bytes(retVal, "utf-8"))
    print(retVal)

conn.close()
print ('Client disconnected!')
