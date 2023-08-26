a = int(input("Type a 'a' value: "))
b = int(input("Type a 'b' value: "))
c = int(input("Type a 'c' value: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("This equation has no real roots")
elif delta == 0:
    print("This equation has one real root")
    x = (-b + delta**(1/2))/(2*a)
    print("\nx =", x)
else:
    print("This equation has two real roots")
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    print("\nx1 =", x1)
    print("\nx2 =", x2)
print("\nEnd of program")