## 실습 20240311-2-1-2
## 1) bool 평가

number1 = 2
number2 = 5
number3 = 7

print("-"*30)
print("실습 20240311-2-1-1 : bool 평가")
print("-"*30)
print(f"{number1} is {number2}  :", number1 is number2)
print(f" {number2}  :", not number2)
print(f"{number1} is not {number2}	:", number1 is not number2)
print(f"{number1} == {number2}		:", number1 == number2)
print(f"{number1} != {number2}		:", number1 != number2)
print(f"{number1} < {number2}		:", number1 < number2)
print(f"{number1} <= {number2}		:", number1 <= number2)
print(f"{number1} > {number2}		:", number1 > number2)
print(f"{number1} >= {number2}		:", number1 >= number2)


## 실습 20240311-2-1-3
## 2) 산술연산

print("-"*30)
print("실습 20240311-2-1-3 : 산술연산")
print("-"*30)
print(f"{number1} + {number2}  :", number1 + number2)
print(f"{number1} - {number2}  :", number1 - number2)
print(f"{number1} * {number2}  :", number1 * number2)
print(f"{number1} / {number2}  :", number1 / number2)
print(f"{number1} ** {number2} :", number1 ** number2)
print(f"{number1} // {number2} :", number1 // number2)
print(f"{number1} % {number2}  :", number1 % number2)


## 실습 20240311-2-1-5
## from, import, as

print("-"*30)
print("실습 20240311-2-1-5 : from, import, as")
print("-"*30)

import datetime
import random as rd
from math import comb

print("datetime.tzinfo()    :", datetime.tzinfo())
print("rd.__name__          :", rd.__name__)
print("comb(5,2)            :", comb(5,2))

## 실습 20240311-2-1-7
## 문자열 포매팅

print("-"*30)
print("실습 20240311-2-1-7 : 문자열 포매팅")
print("-"*30)

print(f"f-string : My favorite number is {number1}")
print("format   : I have {} puddings and {} keyboards".format(number1, number3))
print("%%        : The %s is my Python Learning mate" %("RealWorldPudding"))

## 실습 20240311-2-1-9
## 단일값 타입


print("-"*30)
print("실습 20240311-2-1-9 : 단일값타입")
print("-"*30)

print("type(3)      : ", type(3) )
print("type(3.14)   : ", type(3.14))
print("type(True)   : ", type(True))
print("type(None)   : ", type(None))
print("Ellipsis(...) : ", type(...)) 
print("type(2+4j)   : ", type(2+4j))


## 실습 20240311-2-1-18
## 순서열 공통

print("-"*30)
print("실습 20240311-2-1-18 : 순서열 공통")
print("-"*30)

list1 = [1,1,2,3,5,8,13]
list2 = [10,12,13,14]
def sum(x, y, z):
    return x + y + z

print(f"list : {list1}")
print("색인, index")
print(f"list1[1] : {list1[1]}")
print("슬라이스, slice")
print(f"list1[1:2] : {list1[0:3]}")
print("걸음걸이, step")
print(f"{list1[::2]}")
print("합치기")
print(f"list1.extend(list2) :", list1.extend(list2))
print("곱하기")
print(f"list1*2 :", list1*2)
print("언패킹")
print(f"sum(print(*list1[0:3])) : ", sum(*list1[0:3]))


## 실습 20240311-2-1-10
## 문자열

print("-"*30)
print("실습 20240311-2-1-10 : 문자열")
print("-"*30)

simple_str = 'PuddingCamp'

print(f"문자열 : {simple_str}")

print(f"startswith('Pudding') : ", simple_str.startswith('Pudding'))
print(f"endswith('Pudding') : ", simple_str.endswith('Pudding'))
print(f"format('Pudding') : ", simple_str.startswith('Pudding'))
print(f"isdigit : ", simple_str.isdigit())
print(f"join('python') : ", simple_str.join('135'))
print(f"replace : ", simple_str.replace('P','C'))
print(f"split : ", simple_str.split('g'))
print(f"zfill : ", simple_str.zfill(0))






## 실습 20240311-2-1-11
## 리스트

print("-"*30)
print("실습 20240311-2-1-11 : 리스트")
print("-"*30)

my_list = ['pudding', 'camp', 'echo', 'hello']

print(f"리스트 : {my_list}")

my_list.append('python')
print(f"append : ", my_list)
my_list.clear()
print(f"clear  : ", my_list)
my_list.extend(['pudding', 'real'])
print(f"extend : ", my_list)
my_list.insert(2, ['master'])
print(f"insert : ", my_list)
my_list.pop(2)
print(f"pop    : ", my_list)
my_list.reverse()
print(f"reverse: ", my_list)


## 실습 20240311-2-1-12
## 튜플, Range

print("-"*30)
print("실습 20240311-2-1-12 : 튜플")
print("-"*30)

my_tuple = (1,3,5,7,9)

print(f"튜플 : {my_tuple}")

print(my_tuple[0:3:2])
print(my_tuple[0:-1])
print(my_tuple[::-1])





## 실습 20240311-2-1-15
## dict

print("-"*30)
print("실습 20240311-2-1-15 : dict")
print("-"*30)

menu = {
    "americano" : 1000,
    "latte"     : 1500,
    "hot choco" : 2000,
    "mocha"     : 2000,    
}

print("mocha의 가격은 ? ", menu["mocha"])
# print("menu['greentea'] ", menu["greentea"])


pudding_class = {
    "class_01" : {
        "냠냠이": "1팀",
        "수란"  : "1팀",
        "예선"  : "1팀",
        "젠"    : "1팀",
    },
    "class_02" : {
        "눈커" : "2팀",
        "얼음" : "2팀",
        "의현" : "2팀",
        "조에" : "2팀",
        "희재" : "2팀",
    },
    "class_03" : {
        "강상모" : "3팀",
        "아영" : "3팀",
        "알렉스" : "3팀",
        "애나" : "3팀",
        "Luna" : "3팀",
        "PyoPark" : "3팀",
    }, 
}

print("의현의 소속팀은?  " , pudding_class["class_02"]["의현"])

def function() : 
    """_summary_
    """
    # print("-"*30)
    # print("실습 20240311-2-1-3 : 산술연산")
    # print("-"*30)
    # print(f"{number1} + {number2}  :", number1 + number2)
    # print(f"{number1} - {number2}  :", number1 - number2)
    # print(f"{number1} * {number2}  :", number1 * number2)
    # print(f"{number1} / {number2}  :", number1 / number2)
    # print(f"{number1} ** {number2} :", number1 ** number2)
    # print(f"{number1} // {number2} :", number1 // number2)
    print(f"{number1} % {number2}  :", number1 % number2)


