
class MathDojo:
    def __init__(self):
        self.result = 0
        self.lista = []
        self.counter = 0

    def add(self, num, *nums):
        number = [num]
        for i in nums:
            number.append(i)
            self.counter += 1
            self.lista.append(i)
        for valor in number:
            self.result = self.result + valor
        return self

    def subtract(self, num, *nums):
        number = [num]
        for i in nums:
            number.append(i)
            self.counter += 1
            self.lista.append(-i)
        for valor in number:
            self.result = self.result - valor
        return self

    def desvest(self):
        average = self.result/self.counter
        first_step = (self.result - average)**2
        for valor in self.lista:
            first_step = (valor - average)**2
        self.desviacion = (first_step/self.counter)**(1/2)
        return self

# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).desvest().desviacion
print(x)