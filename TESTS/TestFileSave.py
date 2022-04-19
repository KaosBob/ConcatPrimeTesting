def save(Fname, x):
    f = open(f"Files/{Fname}.txt", "w")
    f.write(str(x))
    f.close()


def read(Fname):
    f = open(f"Files/{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    return x


def concat(a, b):
    return int(f"{a}{b}")


if __name__ == "__main__":
    x = read("TESTX")
    i = read("TESTI")
    while i <= 1243:
        x = concat(x, i)
        i += 1

    save("TESTX", x)
    save("TESTI", i)
    print(x, i)
