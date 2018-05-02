# -*- coding: latin-1 -*-

#
#     Arquivo de Instalacao
#

# Usando setuptools inves de distutils
from setuptools import setup, find_packages
# Encoding consistente 
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Pega a descricao completa a partir do arquivo README
with open(path.join(here, 'README.md'), encoding='latin-1') as f:
    long_description = f.read()

setup(
    name              = 'SuZo',
    version           = '1.0.2',
    description       = 'Um comparador automático para labs do sistema SuSy',
    long_description  = long_description,
    url               = 'https://github.com/muztake/suzo',
    author            = 'Henrique Cunha',
    author_email      = 'henrycunh@gmail.com',
    keywords          = 'comparador parser susy unicamp',
    packages          = find_packages(),
    python_requires   = '>=3',
    install_requires  = ['PyQuery', 'Colorama', 'click'],
    project_urls      = {
        "Twitter"   : "https://twitter.com/henrycunh",
        "Facebook"  : "https://fb.me/henrycunh"
    },
    long_description_content_type = 'text/markdown',
)


