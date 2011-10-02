##Problem 3
##What is the largest prime factor of the number 600851475143?
def factor(n):
    "Generator for getting prime factors for a number"
    yield 1
    i = 2
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            yield i
            n = n / i
            limit = n**0.5
        else:
            i += 1
    if n > 1:
        yield n

def problem3(number=600851475143):
    return max(i for i in factor(number))

if __name__ == '__main__':
    print problem3()
