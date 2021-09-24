#sequencialmente (sem concorrência);
import time, threading, multiprocessing
from random import randint

N = 10000000
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
    
print('Tempo sequencial:')   
print(calcula_tempo_seq(N))
print('=====================================================================================================')

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


num = 4
print('Tempo threading:')   
print(calcula_tempo_thread(num, N))
print('=====================================================================================================')


