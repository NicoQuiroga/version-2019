from generador import generador
adivinado = False
aleatorio = generador(1,20)
while adivinado == False:
    print("ingrese un numero entre 1 y 20")
    numero=int(input())
    if numero == aleatorio :
        print("DALEEEE PURA SANGREEEE!!!!")
        adivinado=True
    if numero<aleatorio :
        print ("pajero, es mas grande")
    if numero >aleatorio:
        print("sos choto vo?, es mas chico")
            
