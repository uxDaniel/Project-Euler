##Problem 2
##By considering the terms in the Fibonacci sequence whose values do not
##exceed four million, find the sum of the even-valued terms.

def fibo(maxnumber, number_list=[1,2]):
    assert(number_list and len(number_list)>=2)
    while number_list[-2]+number_list[-1] <= maxnumber:
        number_list.append(number_list[-2]+number_list[-1])
    return number_list

def problem2(limit=4000000):
    fibonacci_numbers = [1,2]
    return sum(x for x in fibo(limit, fibonacci_numbers) if x%2 == 0)

if __name__ == '__main__':
    print problem2()
