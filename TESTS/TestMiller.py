import random
from timeit import default_timer as timer


# Test 1
def miller_rabin(n):
    r, s = 0, n - 1
    while not(s & 1):
        r += 1
        s >>= 1
    for _ in range(40):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Test 2
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


def isPrime(n):
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(40):
        if (millerTest(d, n) == False):
            return False
    return True


def testFunctions(loopn, printAll=True):
    t = [0, 0]
    s = [0, 0]
    t0 = []
    t1 = []
    n = read("TESTX")
    for i in range(loopn):
        #n = random.getrandbits(128)

        s[0] = timer()
        isPrime(n)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        miller_rabin(n)
        t[1] = timer()-s[1]
        t1.append(t[1])

    avg = []
    r = ["Original", "New"]
    for i in range(2):
        avg.append(eval(f"sum(t{i})/len(t{i})"))
        if printAll:
            print(f"Function: Miller_Rabin_{r[i]}() Avg: {avg[i]}")
    x = avg.index(min(avg))
    print(f"Fastest function was: Miller_Rabin_{r[x]}() Avg: {avg[x]}")


def read(Fname):
    f = open(f"Files/{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    return x


if __name__ == "__main__":
    """ for i in range(10):
        print(f"Starting loop number {i + 1}")
        testFunctions(1, True) """
    start = timer()
    miller_rabin(17)
    end = timer()-start
    print(f"Time taken by function: {end}")
