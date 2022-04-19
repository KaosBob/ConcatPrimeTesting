import random
from timeit import default_timer as timer


def div_mod(n, original_n):
    result = sum(int(digit) for digit in str(n))
    if len(str(result)) > 1:
        result = div_mod(result, original_n)
    else:
        last = int(repr(original_n)[-1])
        text = ""
        if last % 2 == 0:
            text += " 2"
        if result % 3 == 0:
            text += " 3"
        if last % 5 == 0:
            text += " 5"
        if text:
            return True
        else:
            return False
    return result


def is_prime30(n):
    numbers = [1, 7, 11, 13, 17, 19, 23, 29]
    if div_mod(n, n):
        return False
    i = 0
    while i ** 2 <= n:
        for x in numbers:
            if n % (i+x) == 0:
                if (i+x) != 1:
                    return False
        i += 30
    return True


def is_prime6(n):
    if div_mod(n, n):
        return
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def expand_x_1(p):
    ex = [1]
    for i in range(p):
        ex.append(ex[-1] * -(p-i) / (i+1))
    return ex[::-1]


def aks_test(p):
    if p < 2:
        return False
    ex = expand_x_1(p)
    ex[0] += 1
    return not any(mult % p for mult in ex[0:-1])


def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def millerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False


def isPrime(n, k):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(k):
        if (millerTest(d, n) == False):
            return False
    return True


if __name__ == "__main__":
    n = 12345678910987654321  # number to test

    """ print("Started Prime6")
    s1 = timer()
    r1 = is_prime6(n)
    t1 = timer()-s1
    print(f"the number {n} Is Prime\nit took {t1}(Prime6)" if r1 else f"the number {n} Is Not Prime\nit took {t1}(Prime6)")

    print("Started Prime30")
    s2 = timer()
    r2 = is_prime30(n)
    t2 = timer()-s2
    print(f"the number {n} Is Prime\nit took {t2}(Prime30)" if r2 else f"the number {n} Is Not Prime\nit took {t2}(Prime30)")

    print("Started AksTest")
    s3 = timer()
    r3 = aks_test(n)
    t3 = timer()-s3
    print(f"the number {n} is Prime\nit took {t3}(AksTest)" if r3 else f"the number {n} is  Not Prime\nit took {t3}(AksTest)") """

    print("Started MillerTest")
    k = 40  # iterations
    s4 = timer()
    r4 = isPrime(n, k)
    t4 = timer()-s4
    print(f"the number {n} is Prime\nit took {t4}(MillerTest)" if r4 else f"the number {n} is Not Prime\nit took {t4}(MillerTest)")
