#diccionario
traductor = {"casa":"house", "perro":"dog"}
palabra = ""
while palabra !="0":
    palabra = input("Traducir al ingles: ")

    if palabra in traductor:
        print(f"(es) {palabra} : (en) {traductor[palabra]}")
    elif(palabra !="0" and palabra !=""):
        resp = input(f"{palabra} NO EXISTE EN EL DICCIONARIO . ¿deseas traducir s/n?")
        if(resp == "s"):
            traduccion = input(f"ingrese la traduccion de ingles de {palabra}: ")
            if(traduccion !=""):
                traductor[palabra] = traduccion #cargar dict
                


