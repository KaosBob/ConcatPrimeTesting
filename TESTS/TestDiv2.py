import random
from timeit import default_timer as timer


def isEvenXor(n):
    if (n ^ 1 > n):
        return True
    else:
        return False


def isEvenXorBranchless(n):
    return n ^ 1 > n


def isEvenAnd(n):
    if (not(n & 1)):
        return True
    else:
        return False


def isEvenAndBranchless(n):####FASTEST####
    return not(n & 1)


def isEvenOr(n):
    if (n | 1 > n):
        return True
    else:
        return False


def isEvenOrBranchless(n):
    return n | 1 > n


def isEvenString(n):
    if (int(repr(n)[-1]) in (0, 2, 4, 6, 8)):
        return True
    else:
        return False


def isEvenStringBranchless(n):
    return int(repr(n)[-1]) in (0, 2, 4, 6, 8)


def isEvenMod(n):
    if (n % 2 == 0):
        return True
    else:
        return False


def isEvenModBranchless(n):
    return not(n % 2)


def testFunctions(loopn, printAll=True):
    t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t6 = []
    t7 = []
    t8 = []
    t9 = []
    n = read("x")
    for i in range(loopn):
        # n = random.getrandbits(192)

        s[0] = timer()
        isEvenXor(n)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        isEvenXorBranchless(n)
        t[1] = timer()-s[1]
        t1.append(t[1])

        s[2] = timer()
        isEvenAnd(n)
        t[2] = timer()-s[2]
        t2.append(t[2])

        s[3] = timer()
        isEvenAndBranchless(n)
        t[3] = timer()-s[3]
        t3.append(t[3])

        s[4] = timer()
        isEvenOr(n)
        t[4] = timer()-s[4]
        t4.append(t[4])

        s[5] = timer()
        isEvenOrBranchless(n)
        t[5] = timer()-s[5]
        t5.append(t[5])

        s[6] = timer()
        isEvenString(n)
        t[6] = timer()-s[6]
        t6.append(t[6])

        s[7] = timer()
        isEvenStringBranchless(n)
        t[7] = timer()-s[7]
        t7.append(t[7])

        s[8] = timer()
        isEvenMod(n)
        t[8] = timer()-s[8]
        t8.append(t[8])

        s[9] = timer()
        isEvenModBranchless(n)
        t[9] = timer()-s[9]
        t9.append(t[9])

    avg = []
    r = ["Xor", "XorBranchless", "And", "AndBranchless",
         "Or", "OrBranchless", "String", "StringBranchless", "Mod", "ModBranchless"]
    for i in range(10):
        avg.append(eval(f"sum(t{i})/len(t{i})"))
        if printAll:
            print(f"Function: isEven{r[i]}() Avg: {avg[i]}")
    x = avg.index(min(avg))
    print(f"Fastest function was: isEven{r[x]}() Avg: {avg[x]}")


def read(Fname):
    f = open(f"Files/{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    return x


if __name__ == "__main__":
    for i in range(10):
        print(f"Starting loop number {i + 1}")
        testFunctions(1000, False)
