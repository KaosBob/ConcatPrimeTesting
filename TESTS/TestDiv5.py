import random
from timeit import default_timer as timer


def div5(n):
    return int(repr(n)[-1]) in (0, 5)


def div5mod(n):
    return not(int(repr(n)[-1]) % 5)


def div5_Mod(n):
    if (n % 5 == 0):
        return True
    else:
        return False


def div5_ModBranchless(n):
    return n % 5 == 0


def div5ModTest(n):  # FASTEST####
    return not(n % 5)


def testFunctions(loopn, printAll=True):
    t = [0, 0, 0, 0, 0]
    s = [0, 0, 0, 0, 0]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    n = read("x")
    for i in range(loopn):
        # n = random.getrandbits(192)

        s[0] = timer()
        div5(n)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        div5mod(n)
        t[1] = timer()-s[1]
        t1.append(t[1])

        s[2] = timer()
        div5_Mod(n)
        t[2] = timer()-s[2]
        t2.append(t[2])

        s[3] = timer()
        div5_ModBranchless(n)
        t[3] = timer()-s[3]
        t3.append(t[3])

        s[4] = timer()
        div5ModTest(n)
        t[4] = timer()-s[4]
        t4.append(t[4])

    avg = []
    r = ["div5", "div5mod", "div5_Mod", "div5_ModBranchless", "div5ModTest"]
    for i in range(5):
        avg.append(eval(f"sum(t{i})/len(t{i})"))
        if printAll:
            print(f"Function: {r[i]}() Avg: {avg[i]}")
    x = avg.index(min(avg))
    print(f"Fastest function was: {r[x]}() Avg: {avg[x]}")


def read(Fname):
    f = open(f"Files/{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    return x


if __name__ == "__main__":
    for i in range(10):
        print(f"Starting loop number {i + 1}")
        testFunctions(1000, False)
