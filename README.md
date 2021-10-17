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

**Observação:** como o problema fala em número infinito busquei a solução mais simples, que é usar o float('inf'). 
Nos testes, porém, isso se mostra incorreto, uma vez que qualquer inteiro é aceito como float('inf'). 
Por falta de tempo (e por julgar desnecessário fazer isso neste momento), optei por deixar assim.

## Ambiente
- criar um virtualenv com Python >= 3.8
- instalar o pytest

##Commits:
- Initial commit
  - preparação do ambiente
  - Teste apenas com o Erdos
- Commit 1:
  - Criação do Readme
  - Testes com níveis 1 e 2
- Commit 2:
  - Inseri um terceiro nível
  - Os testes passam, mas surge a necessidade de uma recursividade, pois ele atende apenas àquela sequência de publicações
- Commit 3:
  - O dicionário inicializa com erdos com valor zero
  - No laço o autor 'erdos' é ignorado
  - Se o autor está em uma publicação com o erdos, ele necessariamente terá o valor 1
  - A recursividade fica mais clara e o valor de cada autor dependerá, na verdade, do valor mais baixo dos demais autores (será esse valor acrescido de 1)
  
  **Observação:** alterei a ordem dos commits no README para ficarem em ordem cronológica ascendente
- Commit 4:
  - Busca na lista de autores, que é iterada, sua posição, para usá-la posteriormente
  - Cria uma lista de autores sem o autor atual, a fim de buscar o menor índice erdos dentre eles
  - Dentre os colaboradores de um determinado artigo o índice erdos deste colaborador será o menor índice acrescido de 1
- Commit 5:
  - Após revisar, observei que faltava o assert em um dos testes, o que os invalidava
  - Feita a correção do teste sem assert, verifiquei que o script não adicionava 'inf' a autores cujos coautores
  também fossem 'inf'
  - Na lista de índices de coautores adicionei o 'inf'
  - Alterei o valor default do get dos índices de coautores para 'inf'
