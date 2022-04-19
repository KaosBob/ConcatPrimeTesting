from timeit import default_timer as timer


def FizzBuzzA(n):
    return str(n) * (not(not(n % 3 and n % 5))) + "Fizz" * (not(n % 3)) + "Buzz" * (not(n % 5))


def FizzBuzzB(n):
    return str(n) * (n % 3 != 0 and n % 5 != 0) + "Fizz" * (not(n % 3)) + "Buzz" * (not(n % 5))


def FizzBuzzC(n):
    A, B = n % 3, n % 5
    return str(n) * (not(not(A and B))) + "Fizz" * (not(A)) + "Buzz" * (not(B))


def FizzBuzzD(n):
    A, B = n % 3, n % 5
    return str(n) * (A != 0 and B != 0) + "Fizz" * (not(A)) + "Buzz" * (not(B))


def FizzBuzzE(n):
    str = ""
    if not(n % 3):
        str += "Fizz"
    if not(n % 5):
        str += "Buzz"
    if str == "":
        str = n
    return str


def FizzBuzzF(n):  # FASTEST Function
    if not(n % 15):
        return "FizzBuzz"
    elif not(n % 3):
        return "Fizz"
    elif not(n % 5):
        return "Buzz"
    else:
        return n


def testFunctions(loopn, printAll=True):
    t = [0, 0, 0, 0, 0, 0, 0]
    s = [0, 0, 0, 0, 0, 0, 0]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t6 = []
    for i in range(loopn):
        # n = random.getrandbits(192)

        s[0] = timer()
        for n in range(100):
            FizzBuzzA(n)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        for n in range(100):
            FizzBuzzB(n)
        t[1] = timer()-s[1]
        t1.append(t[1])

        s[2] = timer()
        for n in range(100):
            FizzBuzzC(n)
        t[2] = timer()-s[2]
        t2.append(t[2])

        s[3] = timer()
        for n in range(100):
            FizzBuzzD(n)
        t[3] = timer()-s[3]
        t3.append(t[3])

        s[4] = timer()
        for n in range(100):
            FizzBuzzE(n)
        t[4] = timer()-s[4]
        t4.append(t[4])

        s[5] = timer()
        for n in range(100):
            FizzBuzzF(n)
        t[5] = timer()-s[5]
        t5.append(t[5])

        s[6] = timer()  # FASTEST OVERALL
        x = ""
        for n in range(100):
            if not(n % 15):
                x = "FizzBuzz"
            elif not(n % 3):
                x = "Fizz"
            elif not(n % 5):
                x = "Buzz"
            else:
                x = n
        t[6] = timer()-s[6]
        t6.append(t[6])

    avg = []
    r = ["A", "B", "C", "D", "E", "F", "Test"]
    for i in range(7):
        avg.append(eval(f"sum(t{i})/len(t{i})"))
        if printAll:
            print(f"Function: FizzBuzz{r[i]}() Avg: {avg[i]}")
    x = avg.index(min(avg))
    print(f"Fastest function was: FizzBuzz{r[x]}() Avg: {avg[x]}")


if __name__ == "__main__":
    for i in range(10):
        print(f"Starting loop number {i + 1}")
        testFunctions(10000, True)
