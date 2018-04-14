# -*- coding: utf-8 -*-

# Qualquer dúvida me contate
# email     : henrycunh@gmail.com
# facebook  : fb.me/henrycunh
# twitter   : @henrycunh

# Dependencies
from pyquery import PyQuery as pq
from lxml import etree, html
import subprocess
import urllib
import ssl
import re
import os
import sys
import math
from colorama import Fore, Back, Style, init

##################### Utilidades
def printSh(string):
      sys.stdout.write(string)
      sys.stdout.flush()

def clear_str(string):
    s = string
    try:
        s = eval(string)
        return s
    except:
        return s

##################### Raspagem de dados 

# Retorna os inputs e outputs em uma tupla, dado um URL
def getContext(url):
  ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1) # Cria um contexto de SSL, necessária para um request em HTTPS
  url_abs = re.search("(.+\/).+", url).group(1) # Isola o caminho do lab
  page  = html.fromstring(urllib.request.urlopen(url, context = ctx ).read()) # Obtem o html da página de questões do lab 

  pageHtml = pq(page) # Transforma o HTML em uma arvóre de elementos
  raw_links = pq(pageHtml("blockquote blockquote")[0]).find('a') # Pesquisa na árvore por elementos a dentro de um blockquote que esteja dentro de um outro blockquote
  # Definição
  inputs = []
  outputs = []
  count = 0
  total = len(raw_links)
  printSh('\n\t──────────────────────────────────────\n')
  for l in raw_links: # Itera pelos links
    path = pq(l).attr('href') # Obtem o caminho dos links pelo atributo href
    if 'arq' in path: # Verifica se existe arq no link
      # Definindo loading
      percent = (count + 1) / total
      progress = round(percent * 17)
      bar = '%s%s' % (('▓' * progress), ((' ' * (17 - progress))))
      printSh('\r\t  Loading (%3d%%)  ' % (percent * 100) + Fore.RED + bar + Fore.RESET + '   ')
      if '.in' in path: # Arquivo de entrada
        inputs.append(urllib.request.urlopen(url_abs + path, context = ctx).read()) # Insere o corpo do arquivo na lista
      if '.out' in path: # Arquivo de entrada
        outputs.append(urllib.request.urlopen(url_abs + path, context = ctx).read())
    count += 1 # Adiciona ao contador de arquivos lidos
  print('\n\t──────────────────────────────────────')
  return (inputs, outputs)

###############################################################
##################### Ambiente de Runtime #####################
###############################################################

init() # Inicializa o colorama
print(Fore.RED)
print("\t   ██████  █    ██ ▒███████▒ ▒█████  ")
print("\t ▒██    ▒  ██  ▓██▒▒ ▒ ▒ ▄▀░▒██▒  ██▒")
print("\t ░ ▓██▄   ▓██  ▒██░░ ▒ ▄▀▒░ ▒██░  ██▒")
print("\t   ▒   ██▒▓▓█  ░██░  ▄▀▒   ░▒██   ██░")
print("\t ▒██████▒▒▒▒█████▓ ▒███████▒░ ████▓▒░")
print("\t ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ")
print("\t ░ ░▒  ░ ░░░▒░ ░ ░ ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ")
print("\t ░  ░  ░   ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ▒  ")
print("\t       ░     ░       ░ ░        ░ ░  ")
print("\t                   ░                 ")
print(Fore.RESET)
print('\t┌────────┬───────────────────────────┐')
print('\t│ ' + Fore.RED + 'author' + Fore.RESET + ' │ henrique cunha            │')
print('\t│ ' + Fore.RED + 'github' + Fore.RESET + ' │ @muztake                  │')
print('\t│ ' + Fore.RED + 'repo  ' + Fore.RESET + ' │ /suzo                     │')
print('\t│ ' + Fore.RED + 'email' + Fore.RESET + '  │ henrycunh@gmail.com       │')
print('\t├────────┴─────────────────────  ⌠  ─┤')
print('\t│      ' + Fore.RED + 'made with love @ ufscar' + Fore.RESET + '   ⌡   │')
print('\t└────────────────────────────────────┘')
print()
print('\t──────────────────────────────────────')
print('\t  número do lab                      ')
print('\t  > ', end='', flush=1)
problema = input()
print('\t──────────────────────────────────────')
url   = "https://susy.ic.unicamp.br:9999/mc102wy/%s/dados/testes.html" % (problema if len(problema) == 2 else '0' + problema) 
inputs, outputs = getContext(url) # Recebe os inputs e outputs dado o url ajustado ao Lab
print('\n\t──────────────────────────────────────')
print('\t  nome do arquivo                     ')
print('\t  > ', end='', flush=1)
file = input()
print('\t──────────────────────────────────────')
cont = 1
status = []
_outputs = []

print('\n\t┌─────────┬──────────────────────────┐')
for (i, o) in zip(inputs, outputs): # Percorre os inputs e outputs simultaneamente
  # A linha abaixo cria um processo de python, usando uma flag de buffer, e atribuindo tanto à
  # entrada quanto a saída de dados pipes que permitem o envio de dados
  proc = subprocess.Popen(['python','-u', file], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  _o, _i = proc.communicate(i) # Envio o input do problema
  o = str(o, 'utf-8').replace("\r\n","\n") # Converto de bytes para string, e troco os \r\n por \n
  _o = str(_o, 'utf-8').replace("\r\n","\n")
  if(re.search('\(.+\)', _o)): # Muitas vezes linhas de texto são retornadas como tuplas, devido à forma como o print funciona no python, então essa série de comandos (um tanto convolucionados), garante que eles sejam transformados de volta à condição de strings
    _o = list(map(lambda x: clear_str(x), _o.split('\n')))
    _o = '\n'.join(list(map(lambda x: x if type(x) is not tuple else ' '.join(list(map(lambda y: str(y), x))), _o)))
  _outputs.append(_o) # Adiciona o output à lista de outputs fornecidos
  status.append("█" if o == _o else "░") # Adiciona o status do caso à lista de status
  print('\t│ caso %2d │ %-10s' % (cont, (Fore.GREEN + "correto" + Fore.RESET) if _o == o else (Fore.RED + "errado " + Fore.RESET)) + " " * 18 + "│")
  
  cont += 1

print('\t├─────────┴──┬───────────────────────┤')
print("\t│ resultados │ " + Fore.RED + "%s" % (''.join(status)) + Fore.RESET + " ├" + "─" * (21 - cont) +"┤")
print('\t└────────────┴───────────────────────┘')

outputs = list(map(lambda x: str(x, 'utf-8'),outputs)) # Converte os dados de saída experados de bytes em string
print('\n\t──────────────────────────────────────')
print('\t  ver caso teste, ou 0 para sair       ')
print('\t  > ', end='', flush=1)
case = int(input())
print('\t──────────────────────────────────────')
while case > 0:
    if case >= cont:
      print('\n\t──────────────────────────────────────')
      print('\t            fora dos limites          ')
      print('\t──────────────────────────────────────')
      print('\n\t──────────────────────────────────────')
      print('\t  ver caso teste, ou 0 para sair        ')
      print('\t  > ', end='', flush=1)
      case = int(input())
      print('\t──────────────────────────────────────')
      continue
    diff = [i for i in range(len(outputs[case - 1])) if outputs[case - 1][i] != _outputs[case - 1][i]] # Pega todos os indices em que um é diferente do outro
    if len(diff) > 0: # Verifica se existem diferenças
      print('\n\tseu output\n\t', end='')
      for i in range(0, len(_outputs[case - 1])):
            c = _outputs[case - 1][i]
            c = c if c is not '\n' else '\n\t'
            print(Fore.RED + c + Fore.RESET if i in diff else c, end='') # Imprime em vermelho caso seja um indice de diff
      print('\n\toutput esperado\n\t', end='')
      for i in range(0, len(outputs[case - 1])):
            c = outputs[case - 1][i]
            c = c if c is not '\n' else '\n\t'
            print(Fore.RED + c + Fore.RESET if i in diff else c, end='')
    else:
      print('\n\t──────────────────────────────────────')
      print('\t  sem diferenças no caso de teste      ')
      print('\t──────────────────────────────────────')
          
    print('\n\t──────────────────────────────────────')
    print('\t  ver caso teste, ou 0 para sair        ')
    print('\t  > ', end='', flush=1)
    case = int(input())
    print('\t──────────────────────────────────────')