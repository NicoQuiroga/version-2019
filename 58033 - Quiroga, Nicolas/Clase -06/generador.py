import random
def generador (minimo,maximo):
    return random.randint(minimo,maximo)
#if __name__ == "__main__" :
  #  print (generador(1,20))

def generador_mejor(minimo,maximo,lista):
    encontrado = True
    while encontrado:
        aleatorio=random.randint(minimo,maximo)
        encontrado = False
        if aleatorio in lista:
            encontrado=True 
    return aleatorio
print (generador_mejor(3,4,[3])) 