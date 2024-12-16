#Posibles mejoras al código: 
# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minúscula con minúscula
# más de 1 turno con el bucle while

nombre1 = input("¿Cómo se llama el Jugador1? ")
nombre2 = input("¿Cómo se llama el Jugador2? ")

cant_turnos= 3
turno = 0

while turno<cant_turnos:
    jugador1 = input("Hola Jugador1! ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
    jugador2 = input("Hola Jugador2! ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
    user_input1=jugador1.lower()
    user_input2=jugador2.lower()
    
    if user_input1 == user_input2:
        print("¡Ha sido un empate!")
    elif (user_input1 == "piedra" and user_input2 == "tijeras") or (user_input1 == "papel" and user_input2 =="piedra") or (user_input1 == "tijeras" and user_input2 == "papel"):
    # también podría guardar cada condición en una variable y luego el elif quedaría mas simple: "condicion1 or condicion2 or condicion3" 
    # RREFACTORIZACION= mejorar el código para que sea más legible
        print("¡Ha ganado:", nombre1,"!")
    else: 
        print("¡Ha ganado:", nombre2,"!")
    
    turno += 1
if not turno < cant_turnos:
    print("¡Se ha llegado a la cantidad máxima de turnos! Gana quien más turnos haya ganado")