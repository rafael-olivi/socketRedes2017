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

#----- Info Maquina 1 ----------
if form.getvalue('maq1_ps') or form.getvalue('maq1_df')
	or form.getvalue('maq1_finger') or form.getvalue('maq1_uptime'):

	if form.getvalue('maq1_ps'):
		pass
	if form.getvalue('maq1_df'):
		pass
	if form.getvalue('maq1_finger'):
		pass
	if  form.getvalue('maq1_uptime'):
		pass

#Cria a conexao e envia os dados
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(Daemon1)
tcp.send(data)
#Recebe a resposta
resp = s.recv(1024)
s.close()


#----- Info Maquina 2 ----------



#----- Info Maquina 3 ----------







#--------- Mostrar informações --------

print (resp)