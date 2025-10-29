import time

# Função para medir o tempo de execução de cada função
def medir_tempo(func, M, moedas):
    inicio = time.time()
    resultado = func(M, moedas)
    fim = time.time()
    tempo = fim - inicio
    print(f"Função: {func.__name__}")
    print(f"Resultado: {resultado if resultado != float('inf') else -1}")
    print(f"Tempo de execução: {tempo:.6f} segundos\n")
    return resultado, tempo

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


# Função 2:
def qtdeMoedasRec(M, moedas):
    """
    Determina a menor quantidade de moedas necessária para formar o montante M utilizando recursão pura.

    A função tenta todas as combinações possíveis de moedas de forma recursiva,
    retornando o menor número de moedas cuja soma dos valores é exatamente igual a M.
    Caso não seja possível formar o montante, retorna float('inf').

    Parâmetros:
    ----------
    M : int
        O montante total desejado (valor inteiro positivo).
    moedas : list[int]
        Lista contendo os valores das moedas disponíveis. 
        Cada moeda pode ser utilizada um número ilimitado de vezes.

    Retorno:
    -------
    int ou float('inf')
        Retorna o menor número de moedas necessárias para formar o montante M.
        Retorna float('inf') se for impossível formar o montante com as moedas fornecidas.

    Complexidade Teórica:
    ---------------------
    - Tempo:
        O(2^M)  → No pior caso, todas as combinações possíveis são exploradas.
        Ω(1)    → Caso base (M = 0).
        Θ(2^M)  → A função sempre cresce exponencialmente com M (sem otimização).
    - Espaço:
        O(M) → devido à profundidade máxima da pilha de recursão.
    """
    # Caso base: montante zero → nenhuma moeda necessária
    if M == 0:
        return 0
    
    # Se o montante for negativo → combinação inválida
    if M < 0:
        return float('inf')

    # Testa todas as moedas e pega o mínimo de moedas necessário
    menor = float('inf')
    for moeda in moedas:
        qtd = qtdeMoedasRec(M - moeda, moedas)
        if qtd != float('inf'):
            menor = min(menor, 1 + qtd)
    
    # Se não encontrou nenhuma combinação possível
    return menor


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


# Função 4:
def qtdeMoedasPD(M, moedas):
    """
    Determina a menor quantidade de moedas necessária para formar o montante M utilizando Programação Dinâmica (Bottom-Up).

    A função constrói iterativamente um vetor dp onde cada posição i representa
    o menor número de moedas necessário para compor o valor i, considerando todas as moedas disponíveis.

    Parâmetros:
    ----------
    M : int
        O montante total desejado (valor inteiro positivo).
    moedas : list[int]
        Lista contendo os valores das moedas disponíveis.
        Cada moeda pode ser utilizada um número ilimitado de vezes.

    Retorno:
    -------
    int
        Retorna o menor número de moedas necessárias para formar o montante M.
        Retorna -1 se for impossível formar o montante com as moedas fornecidas.

    Complexidade Teórica:
    ---------------------
    - Tempo:
        O(M × n) → Pior e melhor caso, onde n é o número de tipos de moedas.
        Ω(M × n) → Mesmo no melhor caso, todos os subproblemas são processados.
        Θ(M × n) → Crescimento linear em função de M e do número de moedas.
    - Espaço:
        O(M) → Vetor dp de tamanho M + 1.
    """
    # Cria um vetor dp onde dp[i] = menor número de moedas para formar valor i
    dp = [float('inf')] * (M + 1)
    dp[0] = 0  # 0 moedas para formar o montante 0
    
    for i in range(1, M + 1):
        for moeda in moedas:
            if moeda <= i:
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    
    return dp[M] if dp[M] != float('inf') else -1


if __name__ == "__main__":
    moedas = [1, 3, 4]
    M = 35

    medir_tempo(qtdeMoedas, M, moedas)
    medir_tempo(qtdeMoedasRec, M, moedas)
    medir_tempo(qtdeMoedasRecMemo, M, moedas)
    medir_tempo(qtdeMoedasPD, M, moedas)
    
