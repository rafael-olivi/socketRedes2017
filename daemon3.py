#!/usr/bin/env python
import socket
import subprocess

serverSocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
server = '192.168.56.1'
port = 9003
resp = ''
argsBinario = ''
argsString = ''

split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)] #Dividir a string a cada 8 posicoes

#serverSocket.bind((socket.gethostname(), 9001))
serverSocket.bind(('localhost', port))

serverSocket.listen(1)
client, addr = serverSocket.accept()

while 1:
        data = client.recv(1024)
        #print 'Data :', data
        #Process data
        Op = data[72:80] #Protocolo
        if Op == '':
                Op = '0'
        else:
                Op = int(Op, 2) #Converter binario para int

        t = data[16:32]
        if t == '':
                t = 160
        else:
                tam = int(t, 2) #Tamanho do campo Options do cabecalho
        
        args = data[160:tam] #informacao do campo Options

        if (tam > 160):
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
        break

client.close()
serverSocket.shutdown(socket.SHUT_RDWR)
serverSocket.close()