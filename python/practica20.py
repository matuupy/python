usuarios = {"admin":"12345","pepe":"abc123"}
usuario =input("ingrese su usuario: ")
password = input("ingrese su contraseña: ")
intentos = 1
if usuario in usuarios:
    while True:
        if usuarios[usuario] == password:
            print("acceso correcto")
            break
        else:
            intentos = intentos + 1
            if(intentos < 4):
                print(f"error de contraseña, {intentos} de 3")
                password = input("ingrese su contraseña: ")
            else:
                print(f"haz alcnzado los intentos permitidos, {intentos - 1} de 3./cuenta bloqueada. ")
                break
else:
    print("el usuario no existe")

