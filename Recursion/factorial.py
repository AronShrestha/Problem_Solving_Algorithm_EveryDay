import typing


def fac(n:int)->int:
    if n < 3:
        print(n)
        return n
    else:
        
        return n*fac(n-1)
    

print(fac(5))