import socket
import math
import timeit


def parse_data(data):
    try:
        li = data[:-2].split("$ ")
        cmd = li[1][:-1]
        if cmd.lower() == "add":
            return str(float(li[2][:-1]) + float(li[3]))
        elif cmd.lower() == "subtract":
            return str(float(li[2][:-1]) - float(li[3]))
        elif cmd.lower() == "divide":
            return str(float(li[2][:-1]) / float(li[3]))
        elif cmd.lower() == "multiply":
            return str(float(li[2][:-1]) * float(li[3]))
        elif cmd.lower() == "sin":
            return str(math.sin(float(li[2])))
        elif cmd.lower() == "cos":
            return str(math.cos(float(li[2])))
        elif cmd.lower() == "tan":
            return str(math.tan(float(li[2])))
        elif cmd.lower() == "cot":
            return str(math.tan(1 / int(li[2])))
        else:
            return "Not Parsable"
    except ZeroDivisionError:
        return "Division By 0"
    except:
        return "Not Parsable"


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
    start_time = timeit.default_timer()
    val = parse_data(data)
    exec_time = timeit.default_timer() - start_time
    response = val
    print(val)
    if val != "Not Parsable" and val != "Division By 0":
        response = "$ " + str('{:f}'.format(exec_time)) + " $ " + str(val) + " $"
    conn.send(bytes(response, "utf-8"))

conn.close()
print('Client disconnected!')
