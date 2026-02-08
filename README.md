# projeto-de-compiladores

Autora: Joelma Godoy

p1 = Analisador Léxico, Sintático, Semântica e Gerador do Código p2 = Executar o código gerado

Como executar:

1. Tenha um arquivo nomeado codigoPraCompilar.txt no mesmo diretório de p1.py
2. Execute através do comando python p1.py (Isso gerará o código objeto)
3. Execute o código objeto por meio do comando python p2.py (p2.py deve estar no mesmo diretório do código objeto)

Fluxo:
codigoPraCompilar.txt
        ↓
      p1.py
(análise + geração)
        ↓
codigoCompilado.txt
        ↓
      p2.py
 (interpretação)

OBS: A técnica ascendente foi escolhida conforme especificação da Disciplina Projeto de Compiladores, utilizando
controle explícito de pilha sintática, tabela de análise e ações semânticas acopladas
às reduções.
