def genP(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [i for i in range(3, n, 2) if sieve[i]]


def writePrime(n):
    primes = []
    primes = genP(n)
    f = open("Files/Primes.txt", "w")
    for prime in primes:
        f.write(f"{prime}\n")
    f.close()


def readPrime(p):
    f = open("Files/Primes.txt", "r+")
    p = f.readlines()
    f.close()
    for i in range(len(p)):
        p[i] = int(p[i].replace("\n", ""))
    return p


def read(Fname):
    f = open(f"Files/{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    return x


def test():
    x = read("x")
    primes = []
    primes = readPrime(primes)
    for prime in primes:
        if (x % prime == 0):
            return str(prime)
    return "None"


def main():
    writePrime(10_000_000)
    """ primes = []
    primes = readPrime(primes)
    print(primes) """
    # print(test())


if __name__ == "__main__":
    main()
