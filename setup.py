# -*- coding: utf-8 -*-

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
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name              =  'SuZo',
    version           =  '1.0.7',
    description       =  'Um comparador automático para labs do sistema SuSy',
    long_description  =  long_description,
    py_modules        =  ['suzo', 'text', 'utils', 'scraping'],
    entry_points      =  {
        "console_scripts" : [
            'suzo=suzo:cli'
        ]
    },
    url               = 'https://github.com/muztake/suzo',
    author            = 'Henrique Cunha',
    author_email      = 'henrycunh@gmail.com',
    keywords          = 'comparador parser susy unicamp',
    packages          = find_packages(),
    python_requires   = '>=3',
    install_requires  = ['PyQuery', 'Colorama', 'click']
)


