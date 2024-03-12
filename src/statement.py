"""
    푸딩캠프에 오신 걸 환영합니다.
    이 파일은 푸딩캠프의 첫 번째 실습 파일입니다.
"""
    
from datetime import datetime


name    = "의현"
number1 = 299792458
number2 = 149_597_870_700
number3 = 9.80665

HANNALS_FAVORITE_NUMBERS = [number1, number2, number3]

my_favorite_numbers = {2,3,5}

staffs = {
    "hannal"    : "강의자",
    "younamjoo" : "코치",
    "kaycha"    : "코치",
}

def print_puddingcamp_staffs(title, find_role: str) : 
    """푸딩캠프의 스태프 목록을 출력합니다
    
    >>> print_puddingcamp_staffs("title", "코치")
    2
    """
    
    print("*" * 40)
    print(title, datetime.now().isoformat())
    
    count = 0
    for name, role in staffs.items() :
        if role == find_role :
            print(f"\t{name}: {role}")
            count = count + 1
        else :
            print(f"{name}: {role}")
            
        return count
    
if __name__ == "__main__" :
    print_puddingcamp_staffs(
        "푸딩캠프의 스태프 목록은 다음과 같습니다.",
        "코치",
    )