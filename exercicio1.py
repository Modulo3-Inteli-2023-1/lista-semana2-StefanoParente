#  Se achar necessario, faça import de outras bibliotecas




import string

# Crie a função que será avaliada no exercício aqui


def conta_palavras_unicas(list):
    list1 = list.split()
    unicos = []
    for a in list1:
        if a not in unicos:
            unicos.append(a)
    return len(unicos)        






# Teste a sua função aqui (caso ache necessário)











