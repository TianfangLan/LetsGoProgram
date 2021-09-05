def fact(n):
    ''' (int) -> int
    returns the factorial of n
    REQ: n >= 0
    >>> fact(5)
    120
    '''
    if (n == 0):
        result = 1
    else:
        result = n * fact(n-1)
    return result

def find_sum_1(my_list):
    '''(list of int/float) -> int/float
    returns the sum of all items in the list
    REQ: list is not empty
    >>> find_sum_1([5])
    5
    >>> find_sum_1([5, 3, 4])
    12
    '''
    # solve the problem using first approach, where to solve the problem of n 
    # input, solve the problem for n-1 and combine it with the solution where n = 1
    
    # sometimes using a helper function/method is inevitable
    if (len(my_list) == 1):
        result = my_list[0]
    else:
        result = my_list[0] + find_sum_1(my_list[1:])
    return result

def find_sum_2(my_list):
    '''(list of int/float) -> int/float
    returns the sum of all items in the list
    REQ: list is not empty
    >>> find_sum_2([5])
    5
    >>> find_sum_2([5, 3, 4])
    12
    '''
    # solve the problem using the second approach, i.e. divide and conqure
    
    if (len(my_list) == 1):
        result = my_list[0]
    else:
        mid = len(my_list)//2
        result = find_sum_2(my_list[:mid]) + find_sum_2(my_list[mid:])
    return result

def trace_practice(n):
    # this is an example designed for tracing purpose only
    # what is the base case here?
    if (n > 0): 
        print("before " , n);
        trace_practice(n-2);
        trace_practice(n-3);
        print("after ", n, );

def find_avg(my_list):
    '''(list of int/float) -> float
    returns the average of the numbers in my_list
    REQ: my_list is not empty
    >>>find_avg([2, 3, 4])
    3.0
    >>>find_avg([2])
    2.0
    '''
    # we find the solution by calling two helper functions. 
    # in this case the first helper function is recursive (i.e. find_sum_1)
    # len may have been implemented recursively or non-recursively
    result = find_sum_1(my_list)/len(my_list) 
    return result

def find_avg_(my_list, list_size):
    '''(list of int/float, int) -> float
    returns the average of the numbers in my_list
    REQ: my_list is not empty, so list_size >= 1
    >>>find_avg_([1, 2, 3, 4], 4)
    2.5
    >>>find_avg_([2], 1)
    2.0
    '''
    # here we calculte the average of the numbers in my_list without
    # using a helper function. I had to add one parameter to the function
    # so that I can solve the problem recursively.
    if (len(my_list) == 1):
        result =  my_list[0]/list_size
    else:
        result = my_list[0]/list_size + find_avg_(my_list[1:], list_size)
    return result

def count_greater_1(my_list, number):
    '''(list of int, int) -> int
    returns the numbers of integers greater than 'number' in my_list
    >>>count_greater([2, 3, 1, 5 ,6 , 3, 1], 2)
    4
    '''
    if (len(my_list) == 0): 
        result = 0
    else:
        if (my_list[0] > number): 
            result = 1 + count_greater_1(my_list[1:], number) 
        else:
            result = count_greater_1(my_list[1:], number) 
    return result

def count_greater_2(my_list, number):
    '''(list of int, int, int) -> int
    returns the numbers of integers greater than 'number' in my_list
    >>>count_greater([2, 3, 1, 5 ,6 , 3, 1], 2, 0)
    4
    '''
    # this time we use divide and conquer method
    #base case
    if (len(my_list) == 1): 
        result = (my_list[0] > number)
    else:
        mid = len(my_list)//2
        result = count_greater_2(my_list[0:mid], number) + count_greater_2(my_list[mid:], number)
    return result



def is_palindrome(str_input):
    ''' (str) -> bool
    Return True if str_input is a palindrome.
    >>> is_palindrome("")
    True
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("recursion")
    False
    '''
    # examples of palindrome word include noon, civic, radar, level and refer

    if (len(str_input) == 0):
        result = True
    else:
        result = (str_input[0] == str_input[-1]) and is_palindrome(str_input[1:-1])
    return result

def fib(n):
    '''(int) -> int
    returns the nth term in fibonacci sequence
    REQ: n >=0
    >>>fib(4)
    3
    '''
    if (n == 0): 
        result = 0
    elif (n == 1):
        result = 1
    else: 
        result = fib(n-1) + fib(n-2)
    return result

def linear_fib(n):
    '''(int) -> int
    returns the (n-1)th and nth terms in fibonacci sequence for efficiency purpose
    REQ: n >=0
    >>>fib(4)
    (2,3)
    '''
    # trace this function
    if (n == 1): 
        (i, j)  = (0, 1)
    else: 
        (i, j) = linear_fib(n -1)
        (i, j) = ( j , i+ j)
    return (i, j)

if (__name__ == "__main__"):
    print(fact(5))
    print(find_sum_1([2, 3, 4]))
    print(find_sum_2([2, 3, 4]))
    print(find_avg([2, 3, 4]))
    print(find_avg_([1,2, 3, 4], 4))
    print(count_greater_1([2, 3, 1, 5 ,6 , 3, 1], 2))
    print(count_greater_2([2, 3, 1, 5 ,6 , 3, 1], 2))
    trace_practice(5)
    print(fib(10))
    ''' I think you don't want to try this based on what we talked about in the lecture
    print(fib(50))
    '''
    # but try this
    print(linear_fib(50))
