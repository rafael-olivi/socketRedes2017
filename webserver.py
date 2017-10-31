import socket
import cgi
import cgitb; cgitb.enable()
ip = '127.0.0.1'

Daemon1 = (ip, 9001)
Daemon2 = (ip, 9002)
Daemon3 = (ip, 9003)

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

form = cgi.FieldStorage()

data = '' #string de dados que será enviado
resp = '' #resposta da requisicao feita
 
#----- Info Maquina 1 ----------
if form.getvalue('maq1_ps') or form.getvalue('maq1_df')
	or form.getvalue('maq1_finger') or form.getvalue('maq1_uptime'):

	if form.getvalue('maq1_ps'):
		#Protocolo 8 bits
		protocolo = '00000001'
		#Option tamanho variavel
		options1 = form.getvalue('maq1_ps')

	if form.getvalue('maq1_df'):
		protocolo = '00000010'
		options1 = form.getvalue('maq1_df')

	if form.getvalue('maq1_finger'):
		protocolo = '00000011'
		options1 = form.getvalue('maq1_finger')

	if  form.getvalue('maq1_uptime'):
		protocolo = '00000100'
		options1 = form.getvalue('maq1_uptime')

	if options1 = None:
		char = 0
	else:
		char = len(options1)
		#conversao da string em binario
		opBinario = ''.join(format(ord(x), 'b') for x in options1)


# ----- Informações do cabeçalho ---------
#Versao do protocolo 4 bits = 2
version = '0010'
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

#Header_Checksum 16 bits - Verificacao
header_checksum = '0000000000000000'

#Junção das informações 
data += version + IHL + tos + total_length + identification + flags + fOffset
+ ttl + protocolo + header_checksum + s_addr + d_addr + opBinario

#Cria a conexao e envia os dados
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(Daemon1)
tcp.send(data)
#Recebe a resposta
resp += s.recv(1024)
s.close()


#----- Info Maquina 2 ----------



#----- Info Maquina 3 ----------



#--------- Mostrar informações --------

print ("Content-Type: text/html\n\n")
print (resp)