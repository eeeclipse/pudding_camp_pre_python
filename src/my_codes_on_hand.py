"""
    과제-20240311-2
"""
import math 

def find_divisors(a :int) -> list : 
    """
    10진수 정수의 약수를 구하는 함수
    
    Args :
        a (int) : 정수
    
    Returns : 
        list    : 리스트
        
    >>> find_divisors(10)
    [1, 2, 5, 10]
    """
    
    res = []
    
    for i in range(1, a//2 + 1):
        if a % i == 0:
            res.append(i)
    res.append(a)
    
    return res
    
    
    
    