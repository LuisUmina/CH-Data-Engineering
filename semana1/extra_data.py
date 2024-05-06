# NOTES
# soft copy -> reference to another variable
# deep copy -> clone variable independently

# <><><><><><><><><><><><><><><><><><><><><><><><><><>
class Calculator: 
    def __init__(self, name: str) -> None:
        self.name = name

    def calculation(self, n1:int, n2:int, cb:callable) -> any:
        return cb(n1, n2)
    


def mainFirst():
    iteration:list = [ x for x in [1,2,3,4,5] if x%2 != 0]
    print(iteration)

    iteration_Two:list = [ _ for _ in [1,2,3,4,5] if _%2 != 0] # "_" indicates that I don't care about the variable name
    print(iteration_Two)


    def sum(n1:int ,n2:int) -> int:
        return n1 + n2
    
    
    calc = Calculator("Data-engineer")
    print("El calculo es: SUMA, resultado: ", calc.calculation(2,3,sum)) 
    print("El calculo es: RESTA, resultado: ", calc.calculation(2,3, lambda x,y : x-y)) #lambda expression
    print("El calculo es: MULTIPLICACION, resultado: ", calc.calculation(2,3, lambda x,y : x*y)) #lambda expression
    print("El calculo es: DIVISION, resultado: ", calc.calculation(2,3, lambda x,y : x/y)) #lambda expression
    
# MAIN
if __name__ == "__main__":
    mainFirst()





































# class Calculadora:
#     def __init__(self, nombre: str) -> None:
#         self.nombre: str =  nombre
    
#     def calculo(self, n1:int, n2:int, cb:callable) -> any:
#         return cb(n1, n2)



# def main():
#     iteracion:list = [ x for x in [1,2,3,4,5] if x%2 != 0 ]
#     print(iteracion)

#     iteracion_dos:list = [ _ for _ in [1,2,3,4,5] if _%2 != 0 ]
#     print(iteracion_dos)


#     def suma(n:int , n2:int) -> int:
#         return n + n2
    
#     calculin = Calculadora("data-engineer")

#     print("El calculo es: suma, resultado: ",calculin.calculo(2,3,suma))
#     print("El calculo es: resta, resultado: ",calculin.calculo(2,3, lambda x,y : x - y))
#     print("El calculo es: multiplicacion, resultado: ",calculin.calculo(2,3, lambda x,y : x * y))
#     print("El calculo es: division, resultado: ",calculin.calculo(2,3, lambda x,y : x / y))

#     print(id(suma))

# if __name__ == "__main__":
#     main()