class Ternary_Operation():
    def __init__(self, ternary):
        self.ternary= ternary
    

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

A = Ternary_Operation(0)
B = Ternary_Operation(1)
F = Ternary_Operation(2)

C = A+B
D = A*B
E = F.square()

print(A)
print(C)
print(D)
print(E)


