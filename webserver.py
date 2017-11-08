#!/usr/bin/env python
import socket
import cgi, cgitb

ip = '127.0.0.1'

Daemon1 = (ip, 9001)
Daemon2 = (ip, 9002)
Daemon3 = (ip, 9003)

cgitb.enable()

form = cgi.FieldStorage()

options1 = '' #Campo de argumentos do comando da maquina 1
options2 = '' #Campo de argumentos do comando da maquina 2
options3 = '' #Campo de argumentos do comando da maquina 3
data1 = '' #string de dados da maquina 1 que sera enviado
data2 = '' #string de dados da maquina 2 que sera enviado
data3 = '' #string de dados da  maquina 3 que sera enviado
resp1 = '' #resposta da requisicao feita para maquina 1
resp2 = '' #resposta da requisicao feita para maquina 2
resp3 = '' #resposta da requisicao feita para maquina 3

protocolo = ''
opBinario1 = ''
opBinario2 = ''
opBinario3 = ''
opData1 = ''
opData2 = ''
opData3 = ''
total1 = 0
total2 = 0
total3 = 0

#---- Informacoes Fixas do Cabecalho ----------
#Versao do protocolo 4 bits = 2
version = '0010'

#IHL 4 bits 
ihl = '1111'

#Type of service 8 bits = 0
tos = '00000000'

#Identification 16 bits 
identification = '1000000000000000'

#Flags 3 bits - 000 se requisicao
flags = '000'

#Fragment Offset 13 bits = 0
fOffset = '0000000000000'

#Time to live 8 bits = 4
ttl = '00000100'

#Header_Checksum 16 bits - Verificacao
header_checksum = '0000000000000000'

#Source adress 32 bits - 192.168.56.101
s_addr =  '11000000' #192 
s_addr += '10101000' #168 
s_addr += '00111000' #56
s_addr += '01100101' #101

#Destnation adress 32 bits - 192.168.56.1
d_addr =  '11000000' #192
d_addr += '10101000' #168
d_addr += '00111000' #56
d_addr += '00000001'

#Padding 
padding = '00000000'

#----- Info Maquina 1 ----------
if form.getvalue('maq1_ps') or form.getvalue('maq1_df') or form.getvalue('maq1_finger') or form.getvalue('maq1_uptime'):

	if form.getvalue('maq1_ps'):
		#Protocolo 8 bits
		protocolo = '00000001'
		#Option tamanho variavel
		options1 = form.getvalue('maq1-ps')

	if form.getvalue('maq1_df'):
		protocolo = '00000010'
    	options1 = form.getvalue('maq1-df')

    if form.getvalue('maq1_finger'):
        protocolo = '00000011'
        options1 = form.getvalue('maq1-finger')

    if  form.getvalue('maq1_uptime'):
        protocolo = '00000100'
        options1 = form.getvalue('maq1-uptime')

    if (options1 is None):
        c1 = 0  
        #opData = '000000000000000000000000'
    else:
        c1 = len(options1)
        #conversao da string em binario
        opBinario1 = [bin(ord(x))[2:].zfill(8) for x in options1]
        opData1 = opData1.join(opBinario1)

	total1 = 160 + (c1 * 8)

	# ----- Informacoes do cabecalho ---------
	#Total Length 16 bits
	#bl = total.bit_length()
	total_length = 8 * '0' + bin(total1)[2:]
	#total_length = '0000000000000000'

	#Juncao das informacoes 
	data1 += version + ihl + tos + total_length + identification + flags + fOffset + ttl + protocolo + header_checksum + s_addr + d_addr + opData1 + padding

	#Cria a conexao e envia os dados
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(Daemon1)
	s.send(data1)
	#Recebe a resposta
	resp1 += s.recv(1024)
	#print resp
	s.close()

#----- Info Maquina 2 ----------
if form.getvalue('maq2_ps') or form.getvalue('maq2_df') or form.getvalue('maq2_finger') or form.getvalue('maq2_uptime'):

	if form.getvalue('maq2_ps'):
    	#Protocolo 8 bits
    	protocolo = '00000001'
    	#Option tamanho variavel
    	options2 = form.getvalue('maq2-ps')

    if form.getvalue('maq2_df'):
        protocolo = '00000010'
        options2 = form.getvalue('maq2-df')

    if form.getvalue('maq2_finger'):
        protocolo = '00000011'
        options2 = form.getvalue('maq2-finger')

    if  form.getvalue('maq2_uptime'):
        protocolo = '00000100'
        options2 = form.getvalue('maq2-uptime')

    if (options2 is None):
        c2 = 0  
        #opData = '000000000000000000000000'
    else:
        c2 = len(options2)
        #conversao da string em binario
        opBinario2 = [bin(ord(x))[2:].zfill(8) for x in options2]
        opData2 = opData2.join(opBinario2)

	total2 = 160 + (c2 * 8)

	# ----- Informacoes do cabecalho ---------
	#Total Length 16 bits
	#bl = total.bit_length()
	total_length = 8 * '0' + bin(total2)[2:]
	#total_length = '0000000000000000'

	#Juncao das informacoes 
	data2 += version + ihl + tos + total_length + identification + flags + fOffset + ttl + protocolo + header_checksum + s_addr + d_addr + opData2 + padding

	#Cria a conexao e envia os dados
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(Daemon2)
	s.send(data2)
	#Recebe a resposta
	resp2 += s.recv(1024)
	#print resp
	s.close()

#----- Info Maquina 3 ----------
if form.getvalue('maq3_ps') or form.getvalue('maq3_df') or form.getvalue('maq3_finger') or form.getvalue('maq3_uptime'):

	if form.getvalue('maq3_ps'):
    	#Protocolo 8 bits
    	protocolo = '00000001'
    	#Option tamanho variavel
    	options3 = form.getvalue('maq3-ps')

    if form.getvalue('maq3_df'):
        protocolo = '00000010'
        options3 = form.getvalue('maq3-df')

    if form.getvalue('maq3_finger'):
        protocolo = '00000011'
        options3 = form.getvalue('maq3-finger')

    if  form.getvalue('maq3_uptime'):
        protocolo = '00000100'
        options3 = form.getvalue('maq3-uptime')

    if (options3 is None):
        c3 = 0  
        #opData = '000000000000000000000000'
    else:
        c3 = len(options3)
        #conversao da string em binario
        opBinario3 = [bin(ord(x))[2:].zfill(8) for x in options3]
        opData3 = opData3.join(opBinario3)

	total3 = 160 + (c3 * 8)

	# ----- Informacoes do cabecalho ---------
	#Total Length 16 bits
	#bl = total.bit_length()
	total_length = 8 * '0' + bin(total3)[2:]
	#total_length = '0000000000000000'

	#Juncao das informacoes 
	data3 += version + ihl + tos + total_length + identification + flags + fOffset + ttl + protocolo + header_checksum + s_addr + d_addr + opData3 + padding

	#Cria a conexao e envia os dados
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(Daemon3)
	s.send(data3)
	#Recebe a resposta
	resp3 += s.recv(1024)
	#print resp
	s.close()

#--------- Mostrar informacoes --------

print("Content-Type: text/html;charset=utf-8\r\n\r\n")
#print ("Content-Type: text/html\n\n")
print ("<br>Machine #1</br>")
print ("<br>"+resp1+"</br>")
print ("<br>Machine #2</br>")
print ("<br>"+resp2+"</br>")
print ("<br>Machine #3</br>")
print ("<br>"+resp3+"</br>")