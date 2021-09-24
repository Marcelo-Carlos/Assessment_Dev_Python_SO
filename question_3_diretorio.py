#gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes 
# que eles ocupam em disco. Obtenha o nome do diretório do usuário.
# Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco 
# (pode usar as funções sort ou sorted);
#gere um arquivo texto com os valores desta estrutura ordenados.
import os

def exibir_arqs(diretorio):
    lista = diretorio  
    dic = {} 
    for i in lista: 
        if os.path.isfile(i):
            dic[i] = []        
            dic[i] = os.stat(i).st_size
    
    diretorio = os.getcwd()
    print(f"Diretorio: {os.path.basename(diretorio)}") 
    print('==============================================')
        
    titulo = '{:11}'.format("Tamanho")
    titulo = titulo + '{:20}'.format("Nome")    
    print(titulo)
    
    for i in sorted(dic, key = dic.get, reverse=True):
        kb = dic[i]/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))    
        print(tamanho, i)
        
        
exibir_arqs(os.listdir())