Analisando a seguinte linguagem fornecida:

? a
b = a * 2 / (27 - 3)
! a + b
c = a * b

Foi desenvolvida a seguinte gramatica:

Linguagem -> ? id
           | ! Conteudo
           | id = Conteudo

Conteudo -> id resto
          | num resto
          | ( Conteudo )

Resto -> + Conteudo
       | - Conteudo
       | * Conteudo
       | / Conteudo
       | &

Calculando os LA de todas as gramaticas conclui-se que é possivel utilizar um recursivo descendente.
Foi então desenvolvido um analisador sintático, e um léxico para suporte, que processe esta linguagem