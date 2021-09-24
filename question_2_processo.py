#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o
# programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
import subprocess

def abrir_arq(nome):
    subprocess.run(["notepad", nome])
    
arq = input('Digite o nome do arquivo que queira abrir: ')

abrir_arq(arq)