import socket
import psutil

def mostra_uso_memoria():
    mem = psutil.virtual_memory()  
    total = round(mem.total/(1024*1024*1024), 2)
    disponivel = round(mem.available/(1024*1024*1024), 2)
    infos = "Uso de Memoria Total: (" + str(total) + "GB)" + "\nMemoria Disponivel: (" + str(disponivel) + "GB)"
    return infos      
    
udp = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
udp.bind((host, 9999))
print('Esperando receber na porta', 9999, '...')

while True:
    (msg, cliente) = udp.recvfrom(1024)
    msg = msg.decode('ascii')
    resposta = mostra_uso_memoria()        
    udp.sendto(resposta.encode('ascii'), cliente)
udp.close()