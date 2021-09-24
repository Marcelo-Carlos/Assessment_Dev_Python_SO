#Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
#1 15 -42 33 -7 -2 39 8
#19 56 -43 23 -7 -11 33 21 61 9
#Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro 
# elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao 
# segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos 
# que sobrarem do maior devem ser somados a zero.
from itertools import zip_longest

a_txt = []
b_txt = []
    
with open("a.txt", 'r', encoding='utf-8') as arq_lido:
    texto = arq_lido.read().split(' ')
    for j in range(0, len(texto)):
        a_txt.append(int(texto[j]))
                      
with open("b.txt", 'r', encoding='utf-8') as arq_lido:
    texto = arq_lido.read().split(' ')
    for j in range(0, len(texto)):
        b_txt.append(int(texto[j]))
    
somas = [int(e1) + int(e2)  for e1, e2 in zip_longest(a_txt, b_txt, fillvalue=0)]
print(somas)