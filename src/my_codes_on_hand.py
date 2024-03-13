"""
    과제-20240311-2
"""

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

def is_odd(a :int) -> bool : 
    """
    10진수 정수를 입력받아 홀수인지 판별하는 함수
    
    Args :
        a (int) : 정수
    
    Returns : 
        bool    : 홀수 여부
        
    >>> is_odd(5)
    True
    """

    if a // 2 == 0 :
        res = False
    else :
        res = True
    
    return res


def cafe_pudding(cafe_item : str) -> str : 
    """
    푸딩카페 메뉴를 입력하면 가격을 알려주는 함수
    
    Args :
        cafe_item (str) : 메뉴 이름
    
    Returns : 
        str    : 메뉴 가격을 친절하게 안내해주는 문구
        
    >>> cafe_pudding("pudding")
    pudding 은/는 1000 원 이에요.
    """
    menu = {
        "americano" : 1000,
        "latte"     : 1500,
        "hot choco" : 2000,
        "mocha"     : 2000,    
        "pudding"   : 1000,
        "python pudding" : 1500,
        "js   pudding"     : 2000,
        "rust pudding"     : 2000,
    }
    
    if cafe_item in menu.keys() :
        print(f"{cafe_item} 은/는 {menu[cafe_item]} 원 이에요.")
    else : 
        print(f"아직 {cafe_item}은 판매하지 않아요. 다른 메뉴는 어떠세요?")
    
    
    