import socket
import _thread as thread
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

def conectado(con, cliente):
    print('Conectado por ', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)
        msg = input('Digite uma mensagem: ')
        msg = bytes(msg, 'utf-8')
        con.send(msg)

    print('Finalizando conexao do cliente', cliente)
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)
while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))
tcp.close()