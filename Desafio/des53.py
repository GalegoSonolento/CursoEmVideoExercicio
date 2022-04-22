# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Ex: apos a sopa
#A sacada da casa
#o lobo ama o bolo
# anotaram a data da maratona
#Desconsiderar espaços e acentos
termo = str(input('Digite uma tentativa de palíndromo: ')).lower().strip().split()

for i in termo:

