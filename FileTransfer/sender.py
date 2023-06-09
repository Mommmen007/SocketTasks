import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1231))

file = open("cvm.pdf", "rb")
file_size = os.path.getsize("cvm.pdf")

client.send("transferred.pdf".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()