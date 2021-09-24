#usando o módulo threading com 4 threads;
import time, threading
from random import randint

def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

N = 10000
lista = []

for i in range(N):
    lista.append(randint(3, 15))



lista_thread = lista.copy()
vet_threading = []

def soma_fatorial_threading(lista, ini, fim):
    for i in range(ini, fim):
        vet_threading.append(fatorial(lista[i]))
    


def calcula_tempo_thread(Nthreads, N):
    
  # Captura tempo inicial
  t_inicio = float(time.time())

  lista_threads = []
  for i in range(Nthreads):
      ini = i * int(N/Nthreads) # início do intervalo da lista
      fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista
      t = threading.Thread(target=soma_fatorial_threading, args=(lista_thread, ini, fim))
      t.start() # inicia thread
      lista_threads.append(t) # guarda a thread
      
  for t in lista_threads:
      t.join() # Espera as threads terminarem

  # Captura tempo final
  t_fim = float(time.time())
  return t_fim - t_inicio

print(calcula_tempo_thread(6, N))