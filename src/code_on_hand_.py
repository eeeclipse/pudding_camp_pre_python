

## 실습 20240311-2-1-1
## bool 평가

number1 = 299792458
number2 = 149_597_870_700
number3 = 9.80665

print("-"*30)
print("실습 20240311-2-1-1 : bool 평가")
print("-"*30)
print(f"{number1} is {number2}      :", {number1} is {number2})
print(f" {number2}                  :", not number2)
print(f"{number1} is not {number2}	:", number1 is not number2)
print(f"{number1} == {number2}		:", number1 == number2)
print(f"{number1} != {number2}		:", number1 != number2)
print(f"{number1} < {number2}		:", number1 < number2)
print(f"{number1} <= {number2}		:", number1 <= number2)
print(f"{number1} > {number2}		:", number1 > number2)
print(f"{number1} >= {number2}		:", number1 >= number2)