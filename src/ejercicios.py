# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    contador = 0
    for i in range(fil):
        for j in range(col):
            contador += matriz[i][j]
    return contador

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    valor = 0
    for i in range(fil):
        for j in range(col):
            if matriz[i][j] > valor or valor == 0:
                valor = matriz[i][j]
    return valor    

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    transpuesta = []
    for i in range(col):
        fila_transpuesta = []
        for j in range(fil):
            fila_transpuesta.append(matriz[j][i])
        transpuesta.append(fila_transpuesta)
    return transpuesta

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    cant = 0
    for letra in frase:
        if letra == " ":
            cant += 1
    if frase == "":
        return 0
    else:
        return cant + 1

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    tabla = []
    for i in range(1, 11):
        tabla.append(n * i)
    return tabla
    
# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    cant = 0
    for numero in lista:
        if numero < 0:
            cant += 1
    return cant

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    num = len(lista)
    for i in range(num - 1):
        a = lista[i]
        b = lista[i + 1]
        if a > b:
            return False
    return True

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    Alfabeto  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + desplazamiento) % 26
            resultado += alfabeto[nuevo_indice]
        elif letra in Alfabeto:
            indice = Alfabeto.index(letra)
            nuevo_indice = (indice + desplazamiento) % 26
            resultado += Alfabeto[nuevo_indice]
        else:
            resultado += letra
    return resultado

#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass

if __name__ == "__main__":
    main()