import os
import random
import smtplib
import ssl
from email.mime.text import MIMEText

import git

import requests


def genP(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [i for i in range(3, n, 2) if sieve[i]]


def writePrime(n):
    primes = []
    primes = genP(n)
    f = open("Files\\Primes.txt", "w+")
    for prime in primes:
        f.write(f"{prime}\n")
    f.close()


def readPrime(p):
    dirname = f"{os.path.dirname(__file__)}\\Files"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    if not os.path.exists(f"Files\\Primes.txt"):
        writePrime(10_000_000)

    f = open("Files/Primes.txt", "r+")
    p = f.readlines()
    f.close()
    for i in range(len(p)):
        p[i] = int(p[i].replace("\n", ""))
    return p


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


def sendEmail(receivers, subject="Subject not provided", body="Body not provided"):
    if subject == "":
        subject = "Subject not provided"
    if body == "":
        body = "Body not provided"

    sender = "ksb.pymail@gmail.com"
    body = body + "<br><br><br><br><br>Sent by python"

    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(receivers)

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login("ksb.pymail@gmail.com", "pymail123!")
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()


def save(Fname, x):
    f = open(f"Files\\{Fname}.txt", "w")
    f.write(str(x))
    f.close()


def read(Fname, b=0):
    dirname = f"{os.path.dirname(__file__)}\\Files"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    if not os.path.exists(f"Files\\{Fname}.txt"):
        f = open(f"Files\\{Fname}.txt", "w+")
        f.write("1" if b else "2")
        f.close()

    f = open(f"Files\\{Fname}.txt", "r+")
    x = int(f.read())
    f.close()
    try:
        y = int(requests.get(
            f"https://raw.githubusercontent.com/KaosBob/ConcatPrimeTesting/master/Files/{Fname}.txt").text)
    except:
        return x
    return x * (x >= y) + y * (y > x)


def Test(x, i, primes):
    if not(i & 1):
        return "2"
    for prime in primes:
        if (x % prime == 0):
            return str(prime)
    if miller_rabin(x):
        sendEmail(["ksb.test001@gmail.com"], "Prime Number Found!",
                  f"{x} was found to be prime by the MillerTest.<br>Further checking is required")
    else:
        return "MillerTest Failed"


def main():
    x = read("x", 1)
    i = read("i")
    primes = []
    primes = readPrime(primes)
    while True:
        x = int(f"{x}{i}")
        i += 1
        print(
            f"Iteration number {i - 1} is not prime because: {Test(x, i - 1, primes)}")
        save("x", x)
        save("i", i)


if __name__ == "__main__":
    g = git.cmd.Git("https://github.com/KaosBob/ConcatPrimeTesting")
    g.pull()
    # main()
