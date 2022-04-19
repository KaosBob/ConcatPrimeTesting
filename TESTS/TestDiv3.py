import random
from timeit import default_timer as timer


def div3(n):
    result = sum(int(digit) for digit in str(n))
    if result > 9:
        result = div3(result)
    else:
        return result in (3, 6, 9)

    return result


def div3mod(n):
    result = sum(int(digit) for digit in str(n))
    if result > 9:
        result = div3(result)
    else:
        return not(result % 3)

    return result


def div3Test(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n in (3, 6, 9)


def div3TestMod(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return not(n % 3)


def div3_Mod(n):
    if (n % 3 == 0):
        return True
    else:
        return False


def div3_ModBranchless(n):
    return n % 3 == 0


def div3_ModTest(n):####FASTEST####
    return not(n % 3)


def testFunctions(loopn, printAll=True):
    t = [0, 0, 0, 0, 0, 0,0]
    s = [0, 0, 0, 0, 0, 0,0]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t6 = []
    n = read("x")
    for i in range(loopn):
        # n = random.getrandbits(192)

        s[0] = timer()
        div3(n)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        div3mod(n)
        t[1] = timer()-s[1]
        t1.append(t[1])

        s[2] = timer()
        div3Test(n)
        t[2] = timer()-s[2]
        t2.append(t[2])

        s[3] = timer()
        div3TestMod(n)
        t[3] = timer()-s[3]
        t3.append(t[3])

        s[4] = timer()
        div3_Mod(n)
        t[4] = timer()-s[4]
        t4.append(t[4])

        s[5] = timer()
        div3_ModBranchless(n)
        t[5] = timer()-s[5]
        t5.append(t[5])

        s[6] = timer()
        div3_ModTest(n)
        t[6] = timer()-s[6]
        t6.append(t[6])
    avg = []
    r = ["div3", "div3mod", "div3Test", "div3TestMod",
         "div3_Mod", "div3_ModBranchless","div3_ModTest"]
    for i in range(7):
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
