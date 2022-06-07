# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print(f'{texto_1} es mayor')
else:
    print(f'{texto_2} es mayor')

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.

numero_1 = int(texto_1)
numero_2 = int(texto_2)

# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print(f'{numero_1} es mayor')
else:
    print(f'{numero_2} es mayor')

print('\nFin')

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

#Sospecho que es porque respeta el orden en que está organizado el alfabeto. La letra A en primer lugar
#la B en segundo lugar, y así sucesivamente. En este caso Cinco comienza con C que está en tercer lugar
#y Siete con S que está en vigésimo lugar. Sería 3 para "C" y 20 para "S". 20 es mayor a 3, por eso toma
#que siete es mayor a cinco. Es mas fácil deducirlo que explicarlo