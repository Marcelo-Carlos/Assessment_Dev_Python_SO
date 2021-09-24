#Escreva um programa cliente e servidor sobre TCP em Python em que:
#O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente 
# nele.
#O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta 
# ao cliente de volta.
import socket, pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
PORTA = 8888

try:
    socket_cliente.connect((host, PORTA))
    msg = input("Entre com o nome do diretorio no Desktop: ")
    socket_cliente.send(msg.encode('utf-8'))
    resposta = socket_cliente.recv(8192)
    print(pickle.loads(resposta))
    
    
    print("Terminou a busca no servidor...")
    input("Pressione qualquer tecla para sair...")
    
    socket_cliente.close()
except Exception as erro:
    print(str(erro))
   
