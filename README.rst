o susy é chato
--------------

Comparar as saídas dos testes abertos é tão laborioso que ninguém deveria fazer.
Então não faça.

instalação
----------

Os passos abaixo só funcionarão se você tiver o python configurado nas suas váriaveis de ambiente (algo que você definitivamente deveria fazer).

Se não tiver, use esse `tutorial <https://python.org.br/instalacao-windows/>`_.

Abre teu terminal/prompt de cmd, e digita ``pip install suzo``, e é isso ai.

uso
---

Alcance a pasta em que estão os arquivos de código dos lab que você quer comparar, e no terminal, execute ``suzo``.

e.g. supondo que tenho uma pasta contendo meus labs, chamada labs dentro do C:\, então basta executar no terminal/prompt:

.. code-block:: bash

   cd C:\\labs
   suzo

argumentos
----------

--conta         conta/turma em que constam os
                exercícios do susy, e.g. ``suzo --conta mc102qrst``
                o padrão é mc102wy
--pybin         nome do binário do python 3, 
                para execução dos códigos.
                e.g. ``suzo --pybin python3`` 

dá star ai irmão
----------------
Qualquer sugestões, fiquem a vontade para criar um issue. Obrigado c: