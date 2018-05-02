from pyquery import PyQuery as pq
from utils import printSh
from lxml import etree, html
from colorama import Fore
import ssl
import text
import re
import urllib

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
  text.line()
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
      if '.out' in path or '.res' in path: # Arquivo de entrada
        outputs.append(urllib.request.urlopen(url_abs + path, context = ctx).read())
    count += 1 # Adiciona ao contador de arquivos lidos
  print()
  text.line()
  return (inputs, outputs)