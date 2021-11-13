def gcd(x: int, y: int):
    if y == 0:
        return 0
    return gcd(y, x % y)
