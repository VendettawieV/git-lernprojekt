# Einfacher Rechner – Übung 05

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    if b == 0:
        raise ValueError("Division durch 0 nicht erlaubt!")
    return a / b

if __name__ == "__main__":
    print("10 + 5 =", addiere(10, 5))
    print("10 - 5 =", subtrahiere(10, 5))
    print("10 * 5 =", multipliziere(10, 5))
    print("10 / 5 =", dividiere(10, 5))

def potenz(basis, exponent):
    return basis ** exponent
