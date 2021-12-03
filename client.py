import socket
import threading
import sys
import os

nome = input('Qual seu nome: ')
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 5000))


#Parte de enviar mensagens
def conCliente():
    while True:
        try:
            #msg = cliente.recv(1024).decode('utf-8')
            #if msg == "Nome: ":
                #cliente.send(nome.encode('utf-8'))
            enviar = input("")
            if enviar == "y":
                enviar = input("digite uma mensagem:")
                cliente.send(enviar.encode('utf-8'))
            # os.system(msg) #isso ta funcionando mas parece estar com erro
        except:
            print('Deu Ruim')
            cliente.close()
            break


#Quando recebe mensagens
def conServ():
    while True:
        msg = cliente.recv(1024).decode('utf-8')
        if msg == "Nome: ":
            cliente.send(nome.encode('utf-8'))
        else:
            print(msg)
            cliente.send(msg.encode('utf-8'))
            break


# UMA THREAD PARA CADA AÇÃO, RECEBER MENSAGEM E ENVIAR
recebe_thread = threading.Thread(target=conServ)
recebe_thread.start()

envia_thread = threading.Thread(target=conCliente)
envia_thread.start()
