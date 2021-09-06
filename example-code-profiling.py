
def Leibniz4(n):
    sum=0
    new_term=0
    k=1
    for k in range(n):
        k=k+1
        new_term=1/(4*k-3)-1/(4*k-1)
        sum=sum+new_term
    return sum
    

import cProfile
cProfile.run('Leibniz4(10000000)')    