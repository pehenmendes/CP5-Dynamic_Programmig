# CP5 - Dynamic Programming

## Integrantes:
<ul>
  <li>Kayky Silva Stiliano (RM555148)</li>
  <li>Pedro Henrique Mendes (RM555332)</li>
</ul>

<br>

## 1) Introdução e Contextualização do Problema
...

<br>

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
Caso de falha (ilustrado)
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
...

### Função 4 - Usando Programação Dinâmica (Bottom up)
...

<br>

## 3) Conclusão
...
