x = lambda a:a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# los siguientes dos bloques de codigo son iguales
x=(lambda x: x + 1)
print(x(2))

print((lambda x: x + 1)(2))