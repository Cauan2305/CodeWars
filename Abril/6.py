def square_digits(num: int):
    return int("".join([str(int(i) * int(i)) for i in str(num)]))


print(square_digits(765))
"""
    Bem-vindo. Neste kata, você é solicitado 
    a quadrar cada dígito de um número 
        e concatená-los.

    Por exemplo, 
    se executarmos 9119 através da função, 
    811181 será lançado, porque 92 é 81 e 12 é 1. (81-1-1-81)

    Exemplo #2: Uma entrada de 765 irá/deve retornar 493625 
    porque 72 é 49, 62 é 36, e 52 é 25. (49-36-25)

    Nota: A função aceita um inteiro e retorna um inteiro.

    Feliz codificação!

"""
