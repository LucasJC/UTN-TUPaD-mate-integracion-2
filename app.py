def ingresar_dnis():
    # Lucas
    return [ "39057467", "37660974", "36899913", "36493716", "34330039" ]

def generar_conjunto_digitos_unicos(dnis):
    # Mati
    return [[0, 3, 4, 5, 6, 7, 9], [0, 3, 4, 6, 7, 9], [1, 3, 6, 8, 9], [1, 3, 4, 6, 7, 9], [0, 3, 4, 9]]

def ejecutar_operaciones_sobre_conjuntos(numeros_unicos):
    # Macaris
    pass


#Funcion para contar la frecuencia de cada digito en cada DNI
# input a utilizar en la funcion
dnis_completos = [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
# se define la funcion
def contar_frecuencia_digitos(dnis_completos):
    print("Frecuencia de dígitos:")
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


#Funcion para los digitos de cada DNI
# input a utilizar en la funcion        
dnis_completos = [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
def sumar_total_digitos(dnis_completos):
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
    # Nico D
    pass

def expresion_2(numeros_unicos):
    # Nico D
    pass

def ingresar_años_nacimiento():
    # Nico D
    return [1990, 1995, 2000, 2005, 2010]

def contar_nacidos_en_años_pares_e_impares(años_nacimiento):
    # Mati
    pass

def calcular_grupo_z(años_nacimiento):
    # Macaris
    pass

def determinar_años_bisiestos(años_nacimiento):
    # Lucas (Implementar función que determina si un año es bisiesto)
    pass

def calcular_producto_cartesiano(años_nacimiento):
    # Mati
    pass

print("Inicio de ejecución de parte A")

# Ingreso de DNIs por teclado, por defecto tenemos los del grupo:
# [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
dnis = ingresar_dnis()

# Generación de conjuntos de dígitos únicos, cada uno ordenado de menor a mayor. 
# Ejemplo de salida: [[0, 3, 4, 5, 6, 7, 9], [0, 3, 4, 6, 7, 9], [1, 3, 6, 8, 9], [1, 3, 4, 6, 7, 9], [0, 3, 4, 9]]
# Para entrada: [ "39057467", "37660974", "36899913", "36493716", "34330039" ]
numeros_unicos = generar_conjunto_digitos_unicos(dnis)

# Cálculo y visualización de unión, intersección, diferencias y diferencias simétricas
# Imprimirá por pantalla los resultados. Ejemplo: "A U B = {0, 3, 4, 5, 6, 7, 9}"
ejecutar_operaciones_sobre_conjuntos(numeros_unicos)

# Conteo de frecuencia de cada dígito en cada DNI usando estructuras repetitivas
contar_frecuencia_digitos(dnis_completos)

# Suma total de dígitos de cada DNI
sumar_total_digitos(numeros_unicos)

# Expresión lógica 1:
# Si algún conjunto tiene 7 o más dígitos únicos y al menos otro tiene solo 4 o menos, entonces se considera que el 
# grupo es “súper diverso”. En caso de que no se cumplan ambas condiciones a la vez, el grupo es “poco diverso”
expresion_1(numeros_unicos)

# Expresión lógica 2:
# Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces el grupo es "grupo par". En 
# cambio, si hay más conjuntos con cantidad impar de elementos que con cantidad par, entonces se etiqueta como 
# "grupo impar". Finalmente, en caso de empate, etiquetamos al grupo como “grupo de paridad neutra”
expresion_2(numeros_unicos)


print("Inicio de ejecución de parte B")

# Ingreso de años de nacimiento
años_nacimiento = ingresar_años_nacimiento()

# Contar nacidos en años pares e impares
contar_nacidos_en_años_pares_e_impares(años_nacimiento)

# Calcular si es un grupo Z(todos nacieron después del 2000). En caso afirmativo, mostrar mensaje "Grupo Z"
calcular_grupo_z(años_nacimiento)

# Determinar qué años son bisiestos. Si alguno nació en un año bisiesto, debe mostrar mensaje "Tenemos un año especial"
determinar_años_bisiestos(años_nacimiento)

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales
calcular_producto_cartesiano(años_nacimiento)