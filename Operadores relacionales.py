
# Operadores de comparación como < _ > _ <= (menor o igual) >= (mayor o igual)  == (igual) ¡= (diferente) 
#son relacionales que sirven para establecer comparación entre diversos valores.
# Más información en =>>https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/operadores_relacionales.html

saludo1 = "¡Hola!"
saludo2 = "¿Qué tal?"
print ( "\n", saludo1, "\n")

print(" ¿Cómo te llamas?") 
nombre = input()


print( "\n", saludo2, nombre,"\n")

print("¿Cuantos años tienes?" )
edad = int(input())
print("\n")

if edad < 18:
    print( "Estás en la tierna edad", nombre)

elif edad >= 18 and edad<=30:# and es un operador lógico que aqui establece una relación  entre los  valores
    print("Eres una persona hecha y derecha", nombre)

if edad >= 45 and  edad < 65:
    print("Eres Senior, estás en los años de oro de la madurez", nombre)

else:
    print("Estás en la flor dela juventud, tienes mucho por disfrutar", nombre)
