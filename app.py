import datetime

def ingresar_dnis():
    print("\n[Punto A.1 - Ingreso de los DNIs]")
    ingreso = input("Ingresar DNIs separados por coma o bien presionar ENTER para usar los DNIs por defecto: ")
    if ingreso.strip() == "":
        print("Usando DNIs por defecto")
        return [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
        
    else:
        return [ dni.strip() for dni in ingreso.split(",") ]

def generar_conjunto_digitos_unicos(dnis):
    print("\n[Punto A.2 - Generación automática de conjuntos de dígitos únicos]")
    conjuntos = []
    for dni in dnis:
        conjunto = []
        for digito in dni:
            numero = int(digito)
            if numero not in conjunto:
                conjunto.append(numero)
        conjunto.sort()
        conjuntos.append(conjunto)
    print(f"Conjuntos de dígitos únicos generados:\n{conjuntos}")
    return conjuntos

def ejecutar_operaciones_sobre_conjuntos(numeros_unicos):
    print("\n[Punto A.3 - Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica]")
    procesar_operaciones_conjuntos("Unión", union_conjuntos, numeros_unicos)
    procesar_operaciones_conjuntos("Intersección", interseccion_conjuntos, numeros_unicos)
    procesar_operaciones_conjuntos("Diferencia", diferencia_conjuntos, numeros_unicos, False)
    procesar_operaciones_conjuntos("Diferencia simétrica", diferencia_simetrica_conjuntos, numeros_unicos)

# Los operadores |, &, - y ^ en Python están diseñados específicamente para trabajar con conjuntos (sets).
# No funcionan igual con otros tipos de colecciones como listas o tuplas.
# | → Unión de conjuntos
# & → Intersección de conjuntos
# - → Diferencia de conjuntos
# ^ → Diferencia simétrica de conjuntos
# 
# set() recibe un iterable (en este caso una lista) y devuelve un conjunto de elementos unicos.
# el operador | realiza la union de estos dos conjuntos de elementos unicos.
# sorted() recibe un iterable (la union de conjuntos) y devuelve una lista ordenada de manera ascendente.
def union_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) | set(conjunto2))

def interseccion_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) & set(conjunto2))

def diferencia_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) - set(conjunto2))

def diferencia_simetrica_conjuntos(conjunto1, conjunto2):
    return sorted(set(conjunto1) ^ set(conjunto2))

def simbolo_operacion(titulo):
    if titulo == 'Unión':
        return 'U'
    elif titulo == 'Intersección':
        return '∩'
    elif titulo.endswith('simétrica'):
        return 'Δ'
    else:
        return '-'

def imprimir_resultado_operacion(titulo, i, j, resultado):
    simbolo = simbolo_operacion(titulo)
    texto_resultado = '∅' if not resultado else resultado
    print(f"Conjunto {i+1} {simbolo} Conjunto {j+1}: {texto_resultado}")

def procesar_operaciones_conjuntos(titulo, funcion, conjuntos, pares_unicos = True):
    n = len(conjuntos)
    print(f"\n{titulo}:")
    for i in range(n):
        for j in range(n):
            if (pares_unicos and j > i) or (not pares_unicos and i != j):
                resultado = funcion(conjuntos[i], conjuntos[j])
                imprimir_resultado_operacion(titulo, i, j, resultado)

# Función para contar la frecuencia de cada digito en cada DNI
def contar_frecuencia_digitos(dnis_completos):
    print("\n[Punto A.5 - Conteo de frecuencia de cada dígito en cada DNI]")
    # for que recorre cada dni de la lista
    for dni in dnis_completos:
        # se inicializa diccionario para almacenar la frecuencia por cada digito del 0 al 9
        frecuencia_digitos = {
            '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
            '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
        }
        # for que recorre cada digito de los dnis
        for digito in dni:
            # se suma 1 a la frecuencia de cada digito presentado
            if digito in frecuencia_digitos:
                frecuencia_digitos[digito] += 1
        # muestra los resultados por cada dni
        print(f"Para el DNI {dni}, la frecuencia es:")
        for digito, cantidad in frecuencia_digitos.items():
            print(f"Dígito {digito}: {cantidad} veces")

def sumar_total_digitos(dnis_completos):
    print("\n[Punto A.6 - Suma total de los dígitos de cada DNI]")
    # se define la lista vacia resultado para contener la suma de los digitos de cada dni
    resultado = []
    # for para recorrer cada sublista en la lista anidada. digitos_dni es la variable iterativa
    for digitos_dni in dnis_completos:
        # se inicializa la variable suma para guardar el resultado de la suma de los digitos de cada dni
        suma = 0
        # for donde digito es la variable iterativa, recorre cada digito en un dni y acumula la suma de sus valores 
        for digito in digitos_dni:
            suma += int(digito)
        # se agrega el resultado de esta sumatoria al final de la lista resultado
        resultado.append(suma)
        print(f"La suma de los digitos del DNI {digitos_dni} es {suma}")


def expresion_1(numeros_unicos):
    print("\n[Punto A.7 - Evaluación de condiciones lógicas: Expresión 1]")
    hay_grande = any(len(conjunto) >= 7 for conjunto in numeros_unicos)
    hay_chico = any(len(conjunto) <= 4 for conjunto in numeros_unicos)

    if hay_grande and hay_chico:
        print("El grupo es súper diverso")
    else:
        print("El grupo es poco diverso")


def expresion_2(numeros_unicos):
    print("\n[Punto A.7 - Evaluación de condiciones lógicas: Expresión 2]")
    pares = sum(1 for conjunto in numeros_unicos if len(conjunto) % 2 == 0)
    impares = len(numeros_unicos) - pares

    if pares > impares:
        print("El grupo es grupo par")
    elif impares > pares:
        print("El grupo es grupo impar")
    else:
        print("El grupo es grupo de paridad neutra")


def ingresar_años_nacimiento():
    print("\n[Punto B.1 - Ingreso de los años de nacimiento (Si dos o más integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso)]")
    años = []
    cantidad = int(input("¿Cuántos años de nacimiento vas a ingresar? "))
    for i in range(cantidad):
        año = int(input(f"Ingresá el año de nacimiento {i + 1}: "))
        años.append(año)
    return años

def contar_nacidos_en_años_pares_e_impares(años_nacimiento):
    print("\n[Punto B.2 - Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas]")
    pares = 0
    impares = 0

    for año in años_nacimiento:
        if año % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print("Cantidad de nacidos en años pares:", pares)
    print("Cantidad de nacidos en años impares:", impares)

def calcular_grupo_z(años_nacimiento):
    print("\n[Punto B.3 - Si todos nacieron después del 2000, mostrar 'Grupo Z']")
    # TODO implementar
    pass

def es_año_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def determinar_años_bisiestos(años_nacimiento):
    print("\n[Punto B.4 - Si alguno nació en año bisiesto, mostrar 'Tenemos un año especial']")
    for año in años_nacimiento:
        if es_año_bisiesto(año):
            print(f"Tenemos un año especial ({año})")
            return

def calcular_producto_cartesiano(años_nacimiento):
    print("\n[Punto B.5 - Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales]")

    año_actual = datetime.datetime.now().year
    edades = []

    # Se calculan edades actuales a partir del año de nacimiento
    for año in años_nacimiento:
            edad = año_actual - año
            edades.append(edad)

    # Producto cartesiano entre años y edades
    print("Producto cartesiano entre años de nacimiento y edades actuales:")
    for año in años_nacimiento:
            for edad in edades:
                print((año, edad))

def enter_para_continuar():
    input("\nPresione ENTER para continuar...")


print("[Inicio de ejecución de parte A]")

# Ingreso de DNIs por teclado, por defecto tenemos los del grupo:
# [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
dnis = ingresar_dnis()
enter_para_continuar()

# Generación de conjuntos de dígitos únicos, cada uno ordenado de menor a mayor. 
# Ejemplo de salida: [[0, 3, 4, 5, 6, 7, 9], [0, 3, 4, 6, 7, 9], [1, 3, 6, 8, 9], [1, 3, 4, 6, 7, 9], [0, 3, 4, 9]]
# Para entrada: [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
numeros_unicos = generar_conjunto_digitos_unicos(dnis)
enter_para_continuar()

# Cálculo y visualización de unión, intersección, diferencias y diferencias simétricas
# Imprimirá por pantalla los resultados. Ejemplo: "A U B = {0, 3, 4, 5, 6, 7, 9}"
ejecutar_operaciones_sobre_conjuntos(numeros_unicos)
enter_para_continuar()

# Conteo de frecuencia de cada dígito en cada DNI usando estructuras repetitivas
contar_frecuencia_digitos(dnis)
enter_para_continuar()

# Suma total de dígitos de cada DNI
sumar_total_digitos(dnis)
enter_para_continuar()

# Expresión lógica 1:
# Si algún conjunto tiene 7 o más dígitos únicos y al menos otro tiene solo 4 o menos, entonces se considera que el 
# grupo es "súper diverso". En caso de que no se cumplan ambas condiciones a la vez, el grupo es "poco diverso"
expresion_1(numeros_unicos)
enter_para_continuar()

# Expresión lógica 2:
# Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces el grupo es "grupo par". En 
# cambio, si hay más conjuntos con cantidad impar de elementos que con cantidad par, entonces se etiqueta como 
# "grupo impar". Finalmente, en caso de empate, etiquetamos al grupo como "grupo de paridad neutra"
expresion_2(numeros_unicos)
enter_para_continuar()


print("\n\n[Inicio de ejecución de parte B]")

# Ingreso de años de nacimiento
años_nacimiento = ingresar_años_nacimiento()
enter_para_continuar()

# Contar nacidos en años pares e impares
contar_nacidos_en_años_pares_e_impares(años_nacimiento)
enter_para_continuar()

# Calcular si es un grupo Z(todos nacieron después del 2000). En caso afirmativo, mostrar mensaje "Grupo Z"
calcular_grupo_z(años_nacimiento)
enter_para_continuar()

# Determinar qué años son bisiestos. Si alguno nació en un año bisiesto, debe mostrar mensaje "Tenemos un año especial"
determinar_años_bisiestos(años_nacimiento)
enter_para_continuar()

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales
calcular_producto_cartesiano(años_nacimiento)

print("\n[Fin de ejecución]")