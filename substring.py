# -*- coding: UTF-8 -*-

def timesInString(sub, string):
    """
    Calcula el número de veces que sub aparece como una subcadena
    de otra cadena
    """
    contador = 0
    x = len(sub)
    y = len(string)
    i = 0

    while(i <= (y - x)):
        if(string[i:x+i] == sub):
            contador = contador + 1
        i = i + 1

    return contador
    
times = timesInString("aba", "ababa")
print(times)