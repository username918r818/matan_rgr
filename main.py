def f1(x):
    return 1 + x

def f2(x):
    return 1 + x*x*x

def trapezoid(f, a, b, h):
    n = (b - a) / h
    s = 0
    for i in range(1, int(n)):
        s += f(a + i * h)
    return h * (f(a) + 2 * s + f(b)) / 2

def simpson(f, a, b, h):
    n = (b - a) / h
    s = 0
    for i in range(1, int(n)):
        if i % 2 == 0:
            s += 2 * f(a + (i + 1) * h)
        else:
            s += 4 * f(a + i * h)
    return h * (f(a) + s + f(b)) / 3

# h -- шаг
h = 1
a = 0
b = 2

print("Input is:")
print("a = ", a)
print("b = ", b)
print("h = ", h)

print("\nFunction f1")
print("Trapezoid: ", trapezoid(f1, a, b, h))
print("Simpson: ", simpson(f1, a, b, h))
print("The correct is 4")

print("\nFunction f2")
print("Trapezoid: ", trapezoid(f2, a, b, h))
print("Simpson: ", simpson(f2, a, b, h))
print("The correct is 6")