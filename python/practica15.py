class pokemon:
    '''definicion un pokemon'''
#atributos
nombre = None
habilidad = None
tipo = None

#constructor
def __init__(self , n, h, t ):
        self.nombre = n
        self.habilidad = h
        self.tipo = t
#metodos
def verNombre(self):
        return self.nombre

def atacar(self):
        print(f"(self.nombre) ataco")

def defenderse(self):
        print(f"(self.nombre) se defendio")

if __name__ =="__main__":
    pikachu1 = pokemon("pikachu", "trueno","electrico")
    pikachu1.atacar()
    pikachu1.defenderse()

if __name__ =="__main__":
    speak1 = pokemon("pikachu","trueno","electrico")
    speak1.atacar()
    speak1.defenderse()

