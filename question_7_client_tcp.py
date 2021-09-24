#Escreva um programa cliente e servidor sobre UDP em Python que:
#O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e 
# espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes
# (ainda esperando 5s a resposta) antes de desistir.
#O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível
# de memória há no servidor e envia a resposta ao cliente de volta.
import socket, time

HOST = socket.gethostname()
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.settimeout(5)
dest = (HOST, 9999)

msg = "infos memoria"
udp.sendto(msg.encode('ascii'), dest) 
acknowledged = False
cont = 1

while not acknowledged and cont <= 5:
    cont += 1
    try:
        (resposta, server) = udp.recvfrom(1024)
        acknowledged = True
    except socket.timeout:
        udp.sendto(msg.encode('ascii'), dest) 
print(time.ctime())
print(resposta.decode('ascii'))
    
udp.close()

    


    
    
        
        
    
        
udp.close()


