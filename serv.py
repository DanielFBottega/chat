import socket
import threading
import sys, os


HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen()

clientes = []
nomes = []

#manda mensagem para cada cliente, ((((NÃO PODERIA MANDAR PARA SÍ PRÓPRIO))))
def mensagem(msg):
    for cliente in clientes:
        cliente.send(msg)

#Recebe a mensagem e repassa, 
def msgClientes(cliente):
    while True:
        try:
            msg = cliente.recv(1024)
            mensagem(msg)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nome = nomes[index]
            mensagem(f'{nome} saiu do chat'.encode('utf-8'))
            nomes.remove(nome)
            break

#é o main, conecta os clientes
def conexao():
    while True:
        print('Servidor rodando...')
        cliente, endereco = tcp.accept()
        print(f'{str(endereco)} conectado')
        cliente.send('Nome: '.encode('utf-8'))
        nome = cliente.recv(1024)
        nomes.append(nome)
        clientes.append(cliente)
        print(f'*O nome do cliente é: {nome.decode("utf-8")}'.encode('utf-8'))
        mensagem(f'*{nome} Conectou ao chat digite y para enviar uma mensagem ou j para um comando no terminal'.encode('utf-8'))
        thread = threading.Thread(target=msgClientes, args=(cliente,))
        thread.start()


conexao()

