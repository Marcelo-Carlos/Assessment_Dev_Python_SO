from collections import defaultdict
import time, threading, multiprocessing
from random import randint, choice

N = 100000
#N = 1000000

lista = []
for i in range(N):
    lista.append(randint(1,10))
    
def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return fat

def calcula_tempo_seq(N): 
    lista_fat_seq = []   
    t_inicio = float(time.time())
    for i in range(N):
        lista_fat_seq.append(fatorial(lista[i]))
    t_fim = float(time.time())
    
    return t_fim - t_inicio

def soma_fatorial_threading(lista, ini, fim):
    for i in range(ini, fim):
        lista[i] = fatorial(lista[i])
    

def calcula_tempo_thread(Nthreads, N):    
  # Captura tempo inicial
  t_inicio = float(time.time())
   
  
  lista_threads = []
  for i in range(0, Nthreads):
      ini = i * int(N/Nthreads) # início do intervalo da lista
      fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista
      t = threading.Thread(target=soma_fatorial_threading, args=(lista, ini, fim))
      t.start() # inicia thread
      lista_threads.append(t) # guarda a thread
      
  for t in lista_threads:
      t.join() # Espera as threads terminarem

  # Captura tempo final
  t_fim = float(time.time())
  return t_fim - t_inicio

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
        return(fim - inicio)



testes_de_tamanho = [100, 500, 1000]
#testes_de_tamanho = [200, 300, 500, 1000]
testes_de_n_threads = [1, 2, 4]


lista = []
for i in range(N):
    lista.append(randint(1,10))

resultado = defaultdict(list)

for n_thread in testes_de_n_threads:
  for tamanho in testes_de_tamanho:
    if n_thread == 1:     
        resultado = calcula_tempo_seq(tamanho)
        print('N', "  Tamanho", "  Tempo Seq")  
        print(n_thread, " ", tamanho,"      ",  resultado)
    else:
      thread = calcula_tempo_thread(n_thread, tamanho)
      print('N', "  Tamanho", "  Tempo Threading")
      print(n_thread, " ",tamanho, "      ", thread)
      processo = cal_tempo_fat_processo(n_thread, tamanho, lista[:tamanho])
      print('N', "  Tamanho", "  Tempo Multiprocessing")
      print(n_thread, " ",tamanho, "      ", processo)
      
  


