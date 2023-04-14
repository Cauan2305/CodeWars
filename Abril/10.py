def unique_in_order(sequence: list):
    if type(sequence) != list:
        sequence = [i for i in sequence]
    last_value=None
    orderList = []

    for i in sequence:
        if last_value==i:
            pass
        else:
            orderList.append(i)
        last_value=i
    return orderList
print(unique_in_order("ABBCcA"))


"""
Implemente a função unique_in_order que toma como argumento uma sequência 
e retorna uma lista de itens 
sem quaisquer elementos com o mesmo valor 
um ao lado do outro e preservando a ordem original dos elementos.

Por exemplo:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

"""
