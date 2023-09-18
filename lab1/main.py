import math

a = float(input("коэффициент a: "))
b = float(input("коэффициент b: "))
c = float(input("коэффициент c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-D) / (2*a)
    print(
        f"x1 = {realPart} + {imaginaryPart}i, x2 = {realPart} - {imaginaryPart}i")
