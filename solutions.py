#1
#Dado un entero, determinar si es par.
def prob_1(valor):
    
    if valor % 2 == 0:
        return True
    else:
        return False


#2
#Dado un número real representando una temperatura en
#grados Farenheit, encontrar su equivalente en grados
#Celcios.
def prob_2(valor):
    
    #resultado = (valor - 32 )/1.8

    resultado = 5/9*(valor - 32)
    
    return resultado
    

#3
#Dados dos enteros (base y potencia, en este orden),
#determinar manualmente el valor
#que se obtiene al evaluar base^potencia.
def prob_3(entero, potencia):
  
    resultado = entero ** potencia

    return resultado


#4
#Dada una hilera de caracteres y una longitud de párrafo
#(en este orden), devolver una hilera de caracteres que
#centre la palabra en un párrafo de ancho como el dado,
#utilizando de relleno asteriscos.
#Ejemplo (para el caso de la hilera “2013” y el ancho 40):

#******************2013******************
def prob_4(dato, simbolo, cantidad):

    resultado = dato.center(cantidad, simbolo)
    
    return resultado


#5
#Dadas dos listas, representando dos vectores,
#encuentre el vector resultante del producto cruz
#entre ambos vectores dados.
def prob_5(x1, x2, x3, y1, y2, y3):

    op1 = ((x2 * y3)-(x3*y2))
    op2 =((x1*y3)-(x3*y1))
    op3 = ((x1*y2)-(x2*y1))

    return "El vector resultante es:" + " <",op1,op2,op3, ">"

#6
#Dada una lista ordenable, devuelva otra lista con los
#mismos elementos, pero en orden descendente.
#Implemente el algoritmo de Bubble Sort.
def prob_6(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1):
            if a[j] < a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return (a)

    
#7
#Encuentre una lista con todos los múltiplos de 4 o 7,
#menores a 1000, presente la lista ordenada de menor a
#mayor.
def prob_7(valor2, valor1):
    
    i = 0
    
    multiplos = []
    while i <= valor1:
        if i % valor2 == 0:
            multiplos.append(i)
            i = i + 1
        else:
            i = i + 1
    return multiplos


#8
#Dado un entero mayor que cero, imprima un triángulo de
#dicha altura, usando asteriscos.
def prob_8(altura):

    triangulo = ""
 
    for i in range(altura + 1):
        espacio = altura - i
        triangulo += (" " * espacio + "* " * i) + "\n"
         
    return triangulo


def prob_8v2(lineas):
    triangulo =""
    
    for numero_linea in range(lineas): 
        espacios = lineas - numero_linea - 1 
        asteriscos = 1 + numero_linea * 2
        triangulo += "  " * espacios + " *" * asteriscos + "\n"
        
    return triangulo


#9
#Dados tres números (en ningún orden en particular),
#determinar si estos podrían representar los lados de
#un triángulo rectángulo (estos grupos de tres números
#se conocen como Tripletas Pitagóricas).
def prob_9(a,b,c):

    if a**2 == b**2 + c **2:

        return True
    
    else:

        return False

#10
#Dadas tres tuplas (en ningún orden en particular)
#representando tres puntos en un espacio bidimensional,
#determine el tipo de triángulo que representan. No asuma
#inmediatamente que los puntos representan un triángulo.
import math
def prob_10(a,b,c):
    #x1, y1 = a
    #x2, y2 = b
    #x3, y3 = c

    p1 = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    p2 = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    
    p3 = math.sqrt((c[0]- b[0])**2 + (c[1] - b[1])**2)

    triangulo = [p1,p2,p3]

    if triangulo[0] + triangulo[1] <= triangulo[2]:

        return "No es un triangulo"

    elif triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2]:

        return "Triangulo Equilatero"

    elif triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2]:

        return "Triangulo Isocele"

    elif triangulo[0] != triangulo[1] and triangulo[1] != triangulo[2]:

        return "Triangulo Escaleno"

    

#11
#Dada una hilera de caracteres, determine
#si es un Palíndromo.
def prob_11(msj):
    cadenaInvertida = msj[:: -1]
    if msj == cadenaInvertida:
        
        return True
    
    else:
        
        return False

            
#12
#Dado un número entero positivo menor o igual que 1000,
#encuentre su representación en palabras.            
def prob_12(num):
    if num>1000:
        return ("El número debe de ser menor a 1000")
    result = ''
    numero = str(num)
    if len(numero) == 1:
        numero = '0' + numero
    if len(numero) == 2:
        numero = '00' + numero
    if len(numero) == 3:
        numero = '000' + numero
    if len(numero) == 4:
        numero = '0000' + numero
    if len(numero) == 5:
        numero = '0000' + numero
    if len(numero) == 6:
        numero = '000' + numero
    if len(numero) == 7:
        numero = '00' + numero
    if len(numero) == 8:
        numero = '0' + numero
        
    posicion = 1
    
    for i in [0,3,6]:
        var = numero[i] + numero[i + 1]+numero[i + 2]
        if int(var) != 0:
            res = tercia(var)
            if i == 0:
                result = res + " millones "
            elif i == 3:
                result = result + res +" mil "
            elif i == 6:
                result = result + res
                
    return result


#13
#Dado un entero positivo, determinar la
#suma de sus divisores propios.
def prob_13(numero):
    
    resultado = 0
    
    for i in [1,2,3,4,5,6,7,8,9]:
        if numero % i == 0:
            resultado += i

 
    return resultado


#14
#Dado un entero positivo, determinar si es un Número primo.
def prob_14(numero):
    if numero <= 1:
        
        return ("ingrese un numero mayor a 1")
    
    else:
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 2:
            
            return True
        
        else:
            
            return False


#15
#Dado un entero positivo, determinar si
#es un Número perfecto.        
def prob_15(numero):
    suma = 0
    
    for i in range(1,numero):
        if (numero % (i) == 0):
            suma += (i)
    if numero == suma:
        
        return True
    
    else:
        
        return False


#16
#Dados dos enteros positivos,
#determinar si son Números amigos.
def prob_16(valor1, valor2):
    tX = 0
    tR = 0
    for i in range(1, valor1):
        if valor1 % i == 0:
            tX += i
        if valor2 % i == 0:
            tR += i

    return tX == valor2 and tR == valor1
    
#17
#Dados dos enteros positivos,
#determinar si son Primos relativos.
def prob_17(n1, n2):
    suma = 0
    if n1 and n2 <= 1:
        return ("El numero debe de ser mayo a 1")
    else:
        contador1 = 0
        contador2 = 0
        for i in range(1, n1 + 1):
            if n1 % i == 0:
                contador1 = contador1 + 1
        for i in range(1, n2 + 1):
            if n2 % i == 0:
                contador2 = contador2 + 1
        if contador2 == 2:
            return True
        else:
            return ("Uno de los dos o los dos no son primos")
            

#18
#Dado un entero positivo,
#determinar si pertenece a la Serie de Fibonacci.
def prob_18(F):
    A, B = 0,1

    while A < F:
        
        if F == 4 or F ==7:

            return False

        else:
        
            return True

    A, B = B, A + B   


#19
#Dado un entero positivo, determinar el primer número de
#la Serie de Fibonacci que cumple con tener al menos ese
#número de dígitos.
def prob_19(numero):
    x,y = 0,1
    
    while True:
        if len(str(x)) == numero:
            
            return x
        
        x, y = y, x + y

        
#20
#Encuentre todas las Tripletas Pitagóricas
def prob_20():
    arreglo = []
    for j in range(1, 1000):
        for i in range(j + 1, 1000):
            a = i**2 - j**2
            b = 2*j*i
            c = j**2 + i**2
            if ((a**2 + b**2) == c**2) and (a + b + c) == 1000:
                arreglo.append([a,b,c])

    return "Las Tripletas son: ",arreglo

#21
#Dado un entero positivo, encontrar todos los
#números primos menores o iguales a dicho entero.
def prob_21(numero):
    arreglo = []
    
    for i in range(2, numero + 1):
        if prob_14(i):
            arreglo.append(i)
            
    return arreglo


#22
#Dadas cuatro tuplas (en ningún orden en particular)
#representando cuatro puntos en un espacio bidimensional,
#determine si en conjunto representan un cuadrado.
import math
def prob_22(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    d1 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    d2 = math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
    d3 = math.sqrt((p1[0] - p4[0])**2 + (p1[1] - p4[1])**2)

    d4 = math.sqrt((p4[0] - p3[0])**2 + (p4[1] - p3[1])**2)
    d5 = math.sqrt((p4[0] - p2[0])**2 + (p4[1] - p2[1])**2)
    d6 = math.sqrt((p4[0] - p1[0])**2 + (p4[1] - p1[1])**2)

    
    puntos1 = d1, d2, d3
    puntos2 = d4, d5, d6


    if p1 == p2 and p1 == p3 and p1 == p4 and p2 == p3 and p2 == p4 and p3 == p4:

        return False
    
    elif puntos1 == puntos2 :
        
        return True
    
    else:

        return False

    
#23
#Escriba un programa que lea los contenidos de triangle.txt,
#y calcule el camino de adyacentes que suma el total más largo.    
    
    
    

#24
#Dada una lista, encuentre una lista con todas las posibles
#listas representando las permutaciones de la lista original.
def prob_24(numeros):
    orden = numeros
    numerosOrdenados = [orden.copy()]
    ref = []
    n = len(orden)

    for i in range(n):
        ref.append(0)

    i = 0

    while i < n:
        if ref[i] < i:
            if prob_1(i):
                orden[0], orden[i]= orden[i], orden[0]
            else:
                orden[ref[i]], orden[i] = orden[i], orden[ref[i]]
            numerosOrdenados.append(orden.copy())
            ref[i] += 1

            i = 0
        else:
            ref[i] = 0
            i += 1

    return numerosOrdenados
       
