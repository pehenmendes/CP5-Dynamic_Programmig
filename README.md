# CP5 - Dynamic Programming

## Integrantes:
<ul>
  <li>Kayky Silva Stiliano (RM555148)</li>
  <li>Pedro Henrique Mendes (RM555332)</li>
</ul>

<br>

## 1) Introdução e Contextualização do Problema
...

## 2) Análise Detalhada das Abordagens

### Função 1 - Iterativa (estratégia gulosa)
Explicação da lógica (passo a passo):
<ul>
  <li>Filtramos moedas inválidas (<=0) e garantimos que temos tipos válidos.</li>
  <li>Ordenamos as moedas em ordem decrescente (maior primeiro).</li>
  <li>Para cada moeda, pegamos a máxima quantidade inteira possível (qtd = restante // moeda) e subtraímos do restante.</li>
  <li>Continuamos até acabar as moedas ou o restante ficar zero.</li>
  <li>Se ao final restante == 0, retornamos o total de moedas; caso contrário, retornamos -1 (impossível).</li>
</ul>

Por que o algoritmo guloso não garante solução ótima?
A estratégia gulosa toma decisões locais (usar sempre a maior moeda possível naquele momento) sem considerar efeitos futuros. Em alguns sistemas de moedas (por exemplo, o sistema monetário canônico como [1,5,10,25] em que o guloso funciona para moedas típicas), o guloso produz sempre o ótimo. Porém, para conjuntos arbitrários de moedas, a escolha local ótima pode bloquear combinações melhores que usam mais moedas médias em vez de uma moeda grande + várias pequenas.
<br>
Caso de falha (ilustrado):
<ul>
  <li>Moedas: [1, 3, 4]</li>
  <li>Montante: M = 6</li>
</ul>
Passos do guloso:
<ul>
  <li>Ordena → [4, 3, 1]</li>
  <li>Usa uma moeda 4 (restante = 2)</li>
  <li>Não pode usar 3 → usa duas moedas 1 (restante = 0)</li>
  <li>Total moedas = 3 (4 + 1 + 1)</li>
</ul>
Solução ótima:
<ul>
  <li>Usa duas moedas 3 → total moedas = 2 (3 + 3)</li>
</ul>
Logo, guloso -> 3 moedas (pior), ótimo -> 2 moedas.
<br>
<br>
Observações finais:
<ul>
  <li>A função é simples e rápida para muitos casos práticos, e é uma boa heurística inicial.</li>
  <li>Deve-se sempre verificar se o conjunto de moedas é do tipo "canônico" (ou seja, um sistema onde o guloso é ótimo). 
  Para conjuntos arbitrários, usar PD (bottom-up) ou recursão com memoização (top-down) garante ótima solução.</li>
  <li>Retornei -1 quando é impossível formar o montante exatamente; outra opção seria float('inf') para uso interno, mas -1 é mais interpretável no output final.</li>
</ul>

### Função 2 - Recursiva Pura (sem memoização)
...

### Função 3 - Recursiva com Memoização (Top Down)
Explicação da lógica (passo a passo):
<ul>
  <li>A função tenta resolver o problema de formar o montante M a partir das moedas disponíveis, de forma recursiva: para cada moeda, ela tenta resolver o subproblema M - moeda.</li>
  <li>Caso M seja igual a zero, significa que conseguimos formar o valor exato — portanto, retornamos 0 (nenhuma moeda adicional necessária).</li>
  <li>Caso M seja negativo, quer dizer que passamos do valor desejado — retornamos ∞ (impossível formar).</li>
  <li>Antes de calcular novamente um subproblema, a função verifica se ele já foi resolvido anteriormente e guardado no dicionário memo.</li>
  <li>Se estiver no cache (memo), ela simplesmente reutiliza o resultado, sem recalcular.</li>
  <li>Caso contrário, a função chama-se recursivamente para todas as moedas possíveis, pega o menor resultado (menor número de moedas) e armazena esse valor no dicionário antes de retornar.</li>
</ul>

Conceito:
<br>
A Memoização é uma técnica que consiste em armazenar os resultados de subproblemas já resolvidos para evitar cálculos repetidos.
Na recursão pura, cada chamada pode recalcular os mesmos valores várias vezes (por exemplo, qtdeMoedas(4) pode ser resolvida repetidamente em diferentes ramos da árvore recursiva).
Com a memoização, esses resultados ficam salvos em um cache (dicionário memo), e sempre que o mesmo montante M é solicitado novamente, a função retorna o valor diretamente desse cache — sem refazer toda a recursão.
<br>

Ligação com a Programação Dinâmica (PD)
<br>
A recursão com memoização é considerada uma forma de Programação Dinâmica Top Down.
Isso acontece porque ela segue os dois princípios fundamentais da PD:
<ul>
  <li>Subestrutura ótima: o número mínimo de moedas para formar um montante M depende das soluções ótimas dos montantes menores (M - moeda);</li>
  <li>Subproblemas sobrepostos: muitos subproblemas são repetidos ao longo das chamadas recursivas (por exemplo, calcular qtdeMoedas(2) aparece em vários ramos).</li>
</ul>
A diferença para a PD Bottom-Up é apenas a direção da resolução:
<ul>
  <li>Top-Down (recursiva com memoização): resolve os subproblemas conforme são necessários, armazenando os resultados.</li>
  <li>Bottom-Up (iterativa): resolve todos os subproblemas de baixo para cima (de 0 até M), preenchendo uma tabela.</li>
</ul>

Melhoria na Eficiência:
<br>
Na recursão pura, o mesmo subproblema pode ser resolvido diversas vezes, o que causa reprocessamento exponencial.
Por exemplo, se queremos formar M = 6 com moedas [1, 3, 4], a chamada para qtdeMoedas(3) pode ocorrer várias vezes dentro da árvore recursiva.
<br>
Com a memoização, cada valor de M é calculado apenas uma vez e depois reaproveitado.
Isso transforma uma complexidade exponencial em uma quase linear em relação ao número de subproblemas possíveis.
O cache elimina a redundância e garante que cada subproblema contribua uma única vez para o resultado final.
<br>

Complexidade:
<br>
Tempo:
<ul>
  <li>𝑂(𝑀×𝑛)</li>
</ul>
Onde:
<ul>
  <li>'𝑀' é o montante alvo (quantidade de subproblemas possíveis);</li>
  <li>'𝑛' é o número de tipos de moedas.</li>
</ul>
Cada subproblema é resolvido apenas uma vez e, para cada um, percorremos todas as moedas disponíveis.
<br>
<br>
Espaço:
<ul>
  <li>O(M) devido ao dicionário de memoização e à pilha de recursão.</li>
</ul>
Melhor caso (Ω): 
<ul>
  <li>O(𝑛) — quando M = 0 ou quando todas as respostas já estão memorizadas.</li>
</ul>
Pior caso (O):
<ul>
  <li>𝑂(𝑀×𝑛) - quando precisamos calcular todos os subproblemas.</li>
</ul>
Caso médio (Θ): 
<ul>
  <li>𝑂(𝑀×𝑛)</li>
</ul>
<br>

### Função 4 - Usando Programação Dinâmica (Bottom up)
...

## 3) Conclusão
...
