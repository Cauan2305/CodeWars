def odd_or_even(arr: list[int]):
    return "even" if sum(arr) % 2 == 0 else "odd"



"""
Tarefa:
Dada uma lista de inteiros, determine se a soma de seus elementos é ímpar ou par.

Dê sua resposta como uma correspondência de cadeia de caracteres ou ."odd""even"

Se a matriz de entrada estiver vazia, considere-a como: (matriz com zero).[0]

Exemplos:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
"""
