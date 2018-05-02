# -*- coding: utf-8 -*-
# Dependencies
import click
import subprocess
import sys
import urllib
import re
import os
import text
from pathlib import Path
import math
from utils import printSh, clear_str
from scraping import getContext
from colorama import Fore, init

@click.command()
@click.option(
  '--conta',
  default  = "mc102wy"
)
@click.option(
  '--pybin',
  default = "python"
)

def cli(conta, pybin):
  # Inicializa o colorama
  init() 

  # Imprime o header
  print(text.header)
  # Leitura de Dados
  text.inTxt(f"entre com o número do lab ({conta})")
  try:
    problema = int(input())
    text.line()
  except Exception as e:
    text.line()
    while 1:
      text.inTxt("número inválido, tente novamente")
      try:
        problema = int(input())
        text.line()
        break
      except Exception as e:
        pass

  # Define o URL do problema
  url   = "https://susy.ic.unicamp.br:9999/%s/%02d/dados/testes.html" % (conta, problema) 

  # Tenta acessar o problema
  try:
    inputs, outputs = getContext(url) # Recebe os inputs e outputs dado o url ajustado ao Lab
  except Exception as e:
    if e.args[0] == 'list index out of range': # Checa se existe o problema
      while 1:
        text.inTxt("lab inválido, tente dnv")
        try:
          problema = int(input())
          url   = "https://susy.ic.unicamp.br:9999/%s/%02d/dados/testes.html" % (conta, problema) 
          text.line()
          inputs, outputs = getContext(url) # Recebe os inputs e outputs dado o url ajustado ao Lab
          break
        except Exception as e:
          text.centeredTxt("cheque a conta e o número do lab")
          return
  text.inTxt("nome do arquivo de execução")
  file = input()
  text.line()
  file_path = Path(file)
  while not file_path.is_file():
        text.inTxt("arquivo inexistente, tente dnv")
        file = input()
        text.line()
        file_path = Path(file)
        
    
  # Acumuladores
  cont = 1
  status = []
  _outputs = []
  

  print('\n\t┌─────────┬──────────────────────────┐')
  for (i, o) in zip(inputs, outputs): # Percorre os inputs e outputs simultaneamente
    # A linha abaixo cria um processo de python, usando uma flag de buffer, e atribuindo tanto à
    # entrada quanto a saída de dados pipes que permitem o envio de dados
    proc = subprocess.Popen([pybin,'-u', file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    # Envio o input do problema
    _o, errors = proc.communicate(i)
    if proc.returncode:
          # Checando por erro de encoding
          if "Non-ASCII" in str(errors):
                text.centeredTxt("erro de enconding, adicione", "'# -*- coding: utf-8 -*-' no inicio")
                return
    # Converto de bytes para string, e troco os \r\n por \n
    o = str(o, 'utf-8').replace("\r\n","\n") 
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
  text.inTxt("número do caso teste, ou 0 pra sair")
  case = int(input())
  text.line()
  while case > 0:
      if case >= cont:
        text.centeredTxt("fora dos limites")
        text.inTxt("número do caso teste, ou 0 pra sair")
        case = int(input())
        text.line()
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
        text.centeredTxt("caso teste correto, sem diferenças")
      
      print()
      text.inTxt("número do caso teste, ou 0 pra sair")
      case = int(input())
      text.line()