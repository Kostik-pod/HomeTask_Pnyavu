import math


def quadratic_solution():
    D=b**2-4*a*c
    if D < 0:
        print('Корней нет')
    if D == 0:
        x=(-b)/(2*a)
        print(x)
    if D > 0:
        x1=(-b-math.sqrt(D))/(2*a)
        x2=(-b+math.sqrt(D))/(2*a)
        print(x1)
        print(x2)


def simple_solution():
    x=(-c)/b
    print(x)
    
    
a=int(input('Ввидите коэффициент: a='))
b=int(input('Ввидите коэффициент: b='))
c=int(input('Ввидите коэффициент: c='))    
if a == 0:
    simple_solution()
else:
    quadratic_solution()
print()    
    