import multiprocessing, time
from random import randint

N = 10000000

lista = []
for i in range(N):
    lista.append(randint(1,10))

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return fat

def verifica_fatorial_proc(q_entrada, q_saida):
    lista_fat = q_entrada.get()
    q_saida.put([fatorial(item) for item in lista_fat])
    
def cal_tempo_fat_processo(nP, tamanho, lista):    
    if __name__ == '__main__':
        inicio = float(time.time())
        # Fila de entrada dos processos
        q_entrada = multiprocessing.Queue()
        # Fila de saída dos processos
        q_saida = multiprocessing.Queue()
        lista_processos = []
        for i in range(nP):
            lista_fatiada = lista[i*int(tamanho/nP):(i+1) * int(tamanho/nP)]
            q_entrada.put(lista_fatiada)
            p = multiprocessing.Process(target=verifica_fatorial_proc, args=(q_entrada, q_saida,))
            p.start() # inicia processo 0
            lista_processos.append(p)

        lista_nova = []
        for i in range(nP):
            lista_nova.extend(q_saida.get())
        fim = float(time.time())
        print(fim - inicio) 

 
cal_tempo_fat_processo(4, N, lista[:2000])
