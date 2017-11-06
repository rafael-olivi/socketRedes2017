#!/usr/bin/env python
import socket 
import subprocess

serverSocket = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM)
server = '192.168.56.1'
port = 9001
resp = ''
argsBinario = ''
argsString = ''

split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)] #Dividir a string a cada 8 posicoes

#serverSocket.bind((socket.gethostname(), 9001))
serverSocket.bind(('', 9001))

serverSocket.listen(1)

client, addr = serverSocket.accept()

while True:	
	data = client.recv(1024)
	print 'Data :', data
	#Process data
	Op = data[72:80] #Protocolo
	Op = int(Op, 2) #Converter binario para int
	
	tam = int(data[16:32], 2) #Tamanho do campo Options do cabecalho
	args = data[160:tam] #informacao do campo Options

	if (int(args, 2) != 0):
		argsBinario = split_string(args, 8)
		#Converter de lista de binario para string
		argsString = ''.join([chr(int(x, 2)) for x in argsBinario])

	if Op == 1:
		resp = subprocess.check_output("ps " + argsString, shell=True)
	if Op == 2:
		resp = subprocess.check_output("df " + argsString, shell=True)
	if Op == 3:
		resp = subprocess.check_output("finger " + argsString, shell=True)
	if Op == 4:
		resp = subprocess.check_output("uptime " + argsString, shell=True)

	client.send(resp)

serverSocket.close()