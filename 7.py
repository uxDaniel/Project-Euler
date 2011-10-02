##Problem 7
##What is the 10001st prime number?

def isPrime(n):
    return not [x for x in xrange(2, int(n**0.5)+1) if n%x == 0]

def problem7():
    #start with 3 being the 2nd prime (being 2 the 1st prime)
    candidate = 3
    which = 2
    while which < 10001:
        candidate += 2
        if isPrime(candidate): which += 1
    return candidate

if __name__ == '__main__':
    print problem7()
