def binary_search(array,element, debug=False):
    lower_bound=0
    upper_bound=len(array)-1
    
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound)//2 #integer
        if debug:
            print("Lower bound", lower_bound)
            print("Upper bound", upper_bound)
            print("Middle", middle)
        if element == array[middle]:
            return " Your value is found at the middle at index",middle
        elif element < array[middle]: #lesser condition 
            #no change in lower bound
            upper_bound = middle - 1
        else: #greater condition
            #upper cound remain same
            lower_bound = middle +1
    return " your element isnt availabele in the given array"


