##Problem 1
##Find the sum of all the multiples of 3 or 5 below 1000.

def problem1(limit=1000):
    return sum(x for x in xrange(limit) if (x%3 == 0 or x%5 == 0))

if __name__ == '__main__':
    print problem1()
