"""client to connect to server"""
import socket

print("-------------------------------")
print("---------   WELCOME   ---------")
print("-------------------------------")
try:
    conn = socket.socket()
    conn.connect(("127.0.0.1", 8080))
except:
    print("Error connecting to server")
    exit()

def respond_to_input(inp):
    if inp == "":
        return
    if INP == "quit":
        conn.send(str.encode(INP))
        response = conn.recv(4096)
        print("Server -> " + str(response, "utf-8"))
        exit()
    conn.send(str.encode(INP))
    response = conn.recv(4096)
    print("Server -> " + str(response, "utf-8"))


print("Successfully connected to server. Enjoy the services of server!\n")
while True:
    INP = input("Input -> ")
    respond_to_input(INP)
