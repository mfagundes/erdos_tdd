# Número de Erdos
Foi utilizado [este problema](https://dojopuzzles.com/problems/numero-de-erdos/) do Dojo Puzzles

```
O Número de Erdos é uma homenagem prestada ao grande matemático húngaro Paul Erdos, que publicou em toda sua vida mais artigos do que qualquer outro matemático trabalhando com centenas de colaboradores. Este número, que mede a 'distância colaborativa' entre um autor de um artigo e Paul Erdos, é calculado da seguinte maneira:

Erdos possui o número de Erdos igual a 0;
Um matemático M possui esse número igual a soma de 1 com o menor número de Erdos dos matemáticos que escreveram um artigo junto com M;
Aquele(a) que nunca escreveu nenhum artigo com Erdos ou com algum matemático que tenha escrito com Erdos ou com um matemático que escreveu com outro que tenha escrito com Erdos, e assim sucessivamente, tem número de Erdos infinito.
Existem 511 matemáticos com número de Erdos igual a 1, ou seja, que escreveram artigos em parceria com Erdos. Os matemáticos que escreveram artigos junto com estes, possuem esse número igual a 2, os que escreveram artigos junto com estes últimos, possuem o número igual a 3, e assim por diante.

Escreva um programa que, dada uma lista de publicações e seus autores, calcule o número de Erdos de cada autor.

Este problema foi adaptado de http://br.spoj.pl/problems/NUMERDOS/. A descrição do problema foi reduzida para agilizar o entendimento
```
Optei por usar apenas um arquivo, replicando o modelo do repl.it (perdão pelo trocadilho), uma vez que é sequência do Dojo de 11/10/2021

## Ambiente
- criar um virtualenv com Python >= 3.8
- instalar o pytest

##Commits:
- Commit 2:
  - Inseri um terceiro nível
  - Os testes passam, mas surge a necessidade de uma recursividade, pois ele atende apenas àquela sequência de publicações
- Commit 1:
  - Criação do Readme
  - Testes com níveis 1 e 2
- Initial commit
  - preparação do ambiente
  - Teste apenas com o Erdos