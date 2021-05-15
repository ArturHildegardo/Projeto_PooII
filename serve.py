import socket
host = "localhost"
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print("aguardando conexao")
con, client = serv_socket.accept()
print("Conectando")
print("Aguardando mensagem")

while (True):
	recebe = con.recv(1024)
	print("Cliente: " + recebe.decode())
	enviar = input("Enviar Mensagem:")
	con.send(enviar.encode())
	if (enviar == '' and recebe.decode() == ''):
		print('fim...')
		serv_socket.close()
