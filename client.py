import socket
import threading
import sys, os

nome = input('Qual seu nome: ')
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))

#MENSAGENS RECEBIDAS ENTRAM AQUI
def conServ():
    while True:
        try:
            msg = cliente.recv(1024).decode('utf-8')
            if msg == "Nome: ":
                cliente.send(nome.encode('utf-8'))
            else:
                print(msg)
               # os.system(msg) #isso ta funcionando mas parece estar com erro
        except:
            print('Deu Ruim')
            cliente.close()
            break


#MENSAGENS ENVIADAS ENTRAM AQUI
def conCliente():
    while True:
        x = input(">>")
        if x == "y":
            x = input("Digite a mensagem:")
            msg = f"{nome}:{x}"
            cliente.send(msg.encode('utf-8'))
        elif x == "j":
            x = input("Digite o comando:")
            os.system(x)
        


#UMA THREAD PARA CADA AÇÃO, RECEBER MENSAGEM E ENVIAR
recebe_thread = threading.Thread(target = conServ)
recebe_thread.start()

envia_thread = threading.Thread(target = conCliente)
envia_thread.start()