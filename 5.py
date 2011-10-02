##Problem 5
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a,b):
    "Greatest common divisor"
    return a if b==0 else gcd(b, a % b)

def lcm(a,b):
    "Lowest common multiple"
    return a*b / gcd(a, b)

def problem5(limit=20):
    return reduce(lcm, xrange(2, limit+1))

if __name__ == '__main__':
    print problem5()
