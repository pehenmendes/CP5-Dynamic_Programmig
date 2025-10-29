# FUNÇÃO 1 - Função Iterativa (Estratégia Gulosa)

def qtdeMoedas(M, moedas):
    """
    Determina a menor quantidade de moedas necessária para formar o montante M
    utilizando uma estratégia gulosa (iterativa).

    Estratégia:
        - Ordena as moedas em ordem decrescente.
        - Em cada passo, seleciona a maior moeda possível que não exceda o montante restante.
        - Subtrai o valor da moeda escolhida do montante e incrementa o contador.

    Parâmetros:
        M (int): Valor total do montante a ser formado.
        moedas (list[int]): Lista com os valores das moedas disponíveis (ilimitadas).

    Retorno:
        int: Quantidade mínima de moedas utilizadas, se possível.
             Caso não seja possível formar o montante exato, retorna -1.

    Observação:
        - A estratégia gulosa nem sempre garante o resultado ótimo para todos os conjuntos de moedas.
          Exemplo: moedas = [1, 3, 4], M = 6 → Guloso retorna 3 (4+1+1), mas o ótimo é 2 (3+3).

    Complexidade:
        - Tempo:
            O(n log n)  — para ordenar as moedas.
            O(n)        — para percorrer as moedas.
            ⇒ O(n log n) no total.
        - Espaço:
            O(1) — usa apenas variáveis auxiliares.
        - Melhor caso (Ω): O(n)
        - Pior caso (O): O(n log n)
        - Caso médio (Θ): O(n)
    """
    moedas.sort(reverse=True)
    count = 0
    restante = M

    for moeda in moedas:
        if restante >= moeda:
            qtd = restante // moeda
            count += qtd
            restante -= qtd * moeda

    return count if restante == 0 else -1

print(qtdeMoedas(6, [1, 3, 4]))  # Retorna 3 (não ótimo)
print(qtdeMoedas(6, [1, 2, 5]))  # Retorna 2 (5 + 1)


# FUNÇÃO 2 - ...




# FUNÇÃO 3 - Recursiva com Memoização (Top Down)

def qtdeMoedasRecMemo(M, moedas, memo=None):
    """
    Calcula a menor quantidade de moedas necessária para formar o montante M
    utilizando recursão com memoização (estratégia Top-Down de Programação Dinâmica).

    Estratégia:
        - Resolve o problema de forma recursiva:
          Para cada moeda, tenta formar o montante restante (M - moeda).
        - Utiliza um dicionário (memo) para armazenar os resultados de subproblemas já resolvidos,
          evitando recomputações desnecessárias.

    Parâmetros:
        M (int): Valor total do montante a ser formado.
        moedas (list[int]): Lista com os valores das moedas disponíveis.
        memo (dict): Dicionário usado internamente para armazenar subresultados (cache).

    Retorno:
        int: Menor quantidade de moedas necessária para formar o montante M.
             Retorna -1 caso não seja possível formar o valor exato.

    Complexidade:
        - Tempo:
            O(M * n), onde n é o número de moedas.
            Cada subproblema é resolvido apenas uma vez e há M subproblemas possíveis.
        - Espaço:
            O(M) — devido ao dicionário de memoização e à pilha de recursão.
        - Melhor caso (Ω): O(n)
        - Pior caso (O): O(M * n)
        - Caso médio (Θ): O(M * n)
    """
  
    if memo is None:
        memo = {}

    # Caso base
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    # Verifica cache
    if M in memo:
        return memo[M]

    # Explora todas as opções possíveis de moedas
    menor = float('inf')
    for moeda in moedas:
        qtd = qtdeMoedasRecMemo(M - moeda, moedas, memo)
        if qtd != float('inf'):
            menor = min(menor, 1 + qtd)

    # Armazena resultado no cache
    memo[M] = menor
    return menor if menor != float('inf') else -1

print(qtdeMoedasRecMemo(6, [1, 3, 4]))  # Retorna 2 (3 + 3)
print(qtdeMoedasRecMemo(7, [2, 4]))     # Retorna -1 (impossível)


# FUNÇÃO 4 - ...


