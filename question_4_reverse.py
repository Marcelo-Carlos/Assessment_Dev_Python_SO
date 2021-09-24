#Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.
def ler_arq_contrario(arq):
        txt = open(arq)
        print(txt.read()[::-1])

ler_arq_contrario('teste.txt')