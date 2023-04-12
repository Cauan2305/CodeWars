def spin_words(sentence: str):
    separate_words = sentence.split()
    get_words_more_five_caracter = [word for word in separate_words if len(word) >= 5]
    word_reverted=""
    if get_words_more_five_caracter:
        for word in get_words_more_five_caracter:
            sentence=sentence.replace(word,word_reverted.join(reversed([i for i in word])))
    return sentence



print(spin_words("Hey fellow warriors"))

"""
Problema

    Escreva uma função que absorva uma cadeia de caracteres de uma ou mais palavras 
    e retorne a mesma cadeia de caracteres, mas com todas as palavras de cinco ou 
    mais letras invertidas (assim como o nome deste Kata). 
    As cadeias de caracteres passadas consistirão apenas em letras e espaços. 
    Os espaços serão incluídos somente quando mais de uma palavra estiver presente.

Exemplos:

    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
    spinWords( "This is a test") => returns "This is a test" 
    spinWords( "This is another test" )=> returns "This is rehtona test"

"""
