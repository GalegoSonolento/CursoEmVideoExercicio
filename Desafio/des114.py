#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
#https://pt.stackoverflow.com/questions/413890/como-verificar-se-servidor-est%C3%A1-disponivel-antes-do-request-urlopen-em-python#:~:text=Exemplo%3A,O%20servidor%20est%C3%A1%20indispon%C3%ADvel.%22)

import requests

url = 'http://pudim.com.br/'

status_code = requests.get(url).status_code
if status_code == 200:
  print('\033[34mO site está acessível nesse momento\033[m')
else:
  print('\033[31mO site não está acessível no momento\033[m')
