#%%

class Derivative:
  def __init__(og, f, h=10**(-5)):
      og.f = f
      og.h = float(h)

  def __call__(og, x):
      return (og.f(x+og.h) - og.f(x))/og.h



from math import sin, cos, exp, log

df = Derivative(sin)
x = 0
print("d(sin, 0)=")
print(df(x))

df = Derivative(cos)
x = 0
print("d(cos, 0)=")
print(df(x))

df = Derivative(exp)
x = 0
print("d(exp, 0)=")
print(df(x))

def y(x):
    return x**2

df = Derivative(y)
x = 0
print("d(x^2, 0)=")
print(df(x))

df = Derivative(log)
x = 0
print("d(ln, 0)=")
print(df(x))
