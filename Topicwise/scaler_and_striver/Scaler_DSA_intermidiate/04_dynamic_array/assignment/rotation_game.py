def rotate(A,i):
    lis = []
    n = len(A)
    C = A[::-1]
    i = i % n
    result = (C[0:i])[::-1] + (C[i:])[::-1]
    return result

print(rotate([3,1,2,2],3))

    
    
    
    
    
    