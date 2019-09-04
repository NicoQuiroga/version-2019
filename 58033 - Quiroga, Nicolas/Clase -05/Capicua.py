def palindromo (palabra):
    a=list (palabra.replace(" ",""))
    b=list (palabra.replace(" ",""))
    b.reverse()
    if a==b :
        return True
    return False
if __name__=="__main__":
    print (palindromo("somos o no somos"))
