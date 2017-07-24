class Ternary_Operation():
    def __init__(self, ternary):
        self.ternary= ternary%3
    
    

    def __add__ (self, other): # overrun the addition to use "+"
        sum = self.ternary + other.ternary
        tsum = sum % 3
        
        return Ternary_Operation(tsum)
    
    def __mul__(self, other): #overrun the multiplication to use "*"
        mult = self.ternary * other.ternary
        tmult = mult % 3

        return Ternary_Operation(tmult)

    def square(self):
        square = self.ternary * self.ternary
        tsquare = square % 3

        return Ternary_Operation(tsquare)

    def __str__(self):
        return "%i [Ternary]"%(self.ternary)

A = Ternary_Operation(int(input("A? ")))
B = Ternary_Operation(int(input("B? ")))


C = A+B
D = A*B
E = B.square()

print(A)
print(C)
print(D)
print(E)


