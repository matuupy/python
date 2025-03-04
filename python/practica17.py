from practica16 import Calculadora
#CalculadoraCientifica(Calculadora) hereda de Calculadora
class Calculadoracientifica(Calculadora):
        
        def __init__(self):
                super()

        def factorial(self):
                factorial = 1
                for x in range(1, self.numero1 + 1):
                        factorial = factorial * 1
                return factorial
if __name__ == "__main__":
        casiofx = Calculadoracientifica()
        casiofx.setNumeros(5,2)
        print(casiofx.factorial())

