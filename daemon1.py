import socket 
import subprocess

serverSocket = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM)
server = '127.168.56.1'
port = 9001

serverSocket.bind((socket.gethostname(), 9001))

serverSocket.listen(1)

client, addr = serverSocket.accept()

while True:
	data = client.recv(1024)
	print 'Data :', data
	#Process data
	
	pass
	