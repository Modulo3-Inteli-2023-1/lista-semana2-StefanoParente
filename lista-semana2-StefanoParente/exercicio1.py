#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
import string

def conta_palavras_unicas(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if not word.isdigit()]
    return len(words)






# Teste a sua função aqui (caso ache necessário)











