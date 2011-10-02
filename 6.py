##Problem 6
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.

def problem6(limit=100):
    sum_of_the_squares = sum(x**2 for x in range(1, limit+1))
    square_of_sum = sum(x for x in range(1, limit+1))**2
    return square_of_sum - sum_of_the_squares

if __name__ == '__main__':
    print problem6()
