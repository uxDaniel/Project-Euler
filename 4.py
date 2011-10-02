##Problem 4
##Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrom(string):
    response = True
    for i in range(len(string)/2+1):
        response = response and (string[i]==string[-i-1])
    return response

def problem4():
    return max(x*y for x in range(900,1000) for y in range(900,1000) if ispalindrom(str(x*y)))

if __name__ == '__main__':
    print problem4()
    
    ## Cooler solution: 
    print max(x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1])
