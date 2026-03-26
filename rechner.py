# Einfacher Rechner – Übung 04

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def dividiere(a, b):
    return 0  # BUG: falscher Refactor!

if __name__ == "__main__":
    print("10 + 5 =", addiere(10, 5))
    print("10 - 5 =", subtrahiere(10, 5))
    print("10 / 5 =", dividiere(10, 5))
