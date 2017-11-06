#!/usr/bin/env python
import socket
import cgi, cgitb

ip = '127.0.0.1'

Daemon1 = (ip, 9001)
Daemon2 = (ip, 9002)
Daemon3 = (ip, 9003)

cgitb.enable()

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

form = cgi.FieldStorage()

data = '' #string de dados que sera enviado
resp = '' #resposta da requisicao feita
options1 = ''
protocolo = ''
opBinario = ''
opData = ''
total = 0

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

        if (cmp(options1, '')):
                c = 0  
                #opData = '000000000000000000000000'
        else:
                c = len(options1)
                #conversao da string em binario
                opBinario = [bin(ord(x))[2:].zfill(8) for x in options1]
                opData = opData.join(opBinario)

        total = 160 + (c * 8)

# ----- Informacoes do cabecalho ---------
#Versao do protocolo 4 bits = 2
version = '0010'

#IHL 4 bits 
ihl = '1111'

#Type of service 8 bits = 0
tos = '00000000'

#Total Length 16 bits
        #bl = total.bit_length()
total_length = 8 * '0' + bin(total)[2:]
#total_length = '0000000000000000'

#Identification 16 bits 
identification = '1000000000000000'

#Flags 3 bits - 000 se requisicao
flags = '000'

#Fragment Offset 13 bits = 0
fOffset = '0000000000000'

#Time to live 8 bits = 4
ttl = '00000100'

#TESTE
#protocolo = '00000001'

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


#Juncao das informacoes 
data += version + ihl + tos + total_length + identification + flags + fOffset + ttl + protocolo + header_checksum + s_addr + d_addr + opData + padding

#Cria a conexao e envia os dados
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(Daemon1)
s.send(data)
#Recebe a resposta
resp += s.recv(1024)
#print resp
s.close()

#----- Info Maquina 2 ----------



#----- Info Maquina 3 ----------



#--------- Mostrar informacoes --------

print("Content-Type: text/html;charset=utf-8\r\n\r\n")
#print ("Content-Type: text/html\n\n")
print (resp)