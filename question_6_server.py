import socket, os, pickle

def exibir_arqs(diretorio):
    caminho = '\\Users\\marca\\Desktop'
    end = os.path.join(caminho, diretorio)
    lista = os.listdir(end) 
    lista_arq = [] 
    for i in lista:
        end_i = os.path.join(end, i)
        if os.path.isfile(end_i): 
            lista_arq.append(i) 
    return lista_arq

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                         
PORTA = 8888
socket_servidor.bind((host, PORTA))
socket_servidor.listen()

print("Servidor de nome", host, "esperando conexão na porta", PORTA)

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    
    msg = socket_cliente.recv(8192)
    msg = msg.decode('utf-8')
    resposta = pickle.dumps(exibir_arqs(msg))
    socket_cliente.send(resposta)
    
    
socket_servidor.close()
    
