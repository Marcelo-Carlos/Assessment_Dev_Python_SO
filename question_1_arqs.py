#obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
#imprima o nome do processo e seu PID;
#imprima também o percentual de uso de CPU e de uso de memória.

#exibir processos
import psutil, time, os

def exibir_processos(pid):
    try:
        processos = psutil.Process(pid)
        lista_processo = '{:6}'.format(pid)
        lista_processo = lista_processo + '{:8.2f}'.format(processos.cpu_percent(interval=None))
        lista_processo = lista_processo + '{:10.2f}'.format(processos.memory_percent()) + " MB"
        rss = processos.memory_info().rss/1024/1024
        lista_processo = lista_processo + '{:10.2f}'.format(rss) + " MB"
        vms = processos.memory_info().vms/1024/1024
        lista_processo = lista_processo + '{:10.2f}'.format(vms) + " MB"
        lista_processo = lista_processo + '   ' + processos.name()
        print(lista_processo)
    except:
        pass 

titulo = '{:^7}'.format("PID")
titulo = titulo + '{:^11}'.format("CPU (%)")
titulo = titulo + '{:^12}'.format("Mem. (%)")
titulo = titulo + '{:^12}'.format("RSS")
titulo = titulo + '{:^12}'.format("VMS")
titulo = titulo + '{:^12}'.format("Nome")
print(titulo)

lista = psutil.pids()

for i in lista:
	exibir_processos(i)