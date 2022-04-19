import math
import random
from timeit import default_timer as timer


def concatIntMath(a,b):
    return int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)
    

def concatInt(a, b):
    return a*(10**len(str(b)))+b
    

def concatFString(a, b):####FASTEST####
    return int(f"{a}{b}")


def concatString(a,b):
    return int(str(a) + str(b))
    

def testFunctions(loopn, printAll=True):
    t = [0, 0, 0, 0]
    s = [0, 0, 0, 0]
    r = [0, 0, 0, 0]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    for i in range(loopn):
        n1 = random.getrandbits(32)
        n2 = random.getrandbits(32)

        s[0] = timer()
        r[0] = concatIntMath(n1,n2)
        t[0] = timer()-s[0]
        t0.append(t[0])

        s[1] = timer()
        r[1] = concatInt(n1,n2)
        t[1] = timer()-s[1]
        t1.append(t[1])

        s[2] = timer()
        r[2] = concatFString(n1,n2)
        t[2] = timer()-s[2]
        t2.append(t[2])

        s[3] = timer()
        r[3] = concatString(n1,n2)
        t[3] = timer()-s[3]
        t3.append(t[3])
        
    avg = []
    fn = ["IntMath", "Int", "FString", "String"]
    for i in range(4):
        avg.append(eval(f"sum(t{i})/len(t{i})"))
        if printAll:
            print(f"Function: concat{fn[i]}() Avg: {avg[i]}")
    x = avg.index(min(avg))
    print(f"Fastest function was: concat{fn[x]}() Avg: {avg[x]}")


if __name__ == "__main__":
    for i in range(10):
        print(f"Starting loop number {i + 1}")
        testFunctions(100000, False)