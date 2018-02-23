# returns fibonacci sequence of length x

def fib(x):
    arr = [1,1]
    if x == 1: 
        arr = [1]
        return arr
    elif x == 2:
        return arr
    else: 
        for i in range(3,x+1):
            new = arr[i-2] + arr[i-3]
            arr.append(new)
        return arr 


print(fib(8))