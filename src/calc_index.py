#! /usr/bin/env python

import pytest 
from calc_class import Calculator


def calc_bmi(weight, height):
    """
        Simple BMI Calculator 
        
        info :
            - Pudding Camp Assignment 20240307-1
            
        >>> calc_bmi(64000, 160)
        25
    """
    
    #### todo 
    #     weight  = raw_input("Insert your weight : ")
    #     height  = raw_input("Insert your height : ")
    ####

    nom     = Calculator(height,height).mul()
    res     = Calculator(weight, nom).div()
    
    return print(f"Your BMI is {res}.")



def calc_wacc(E, D, Re, Rd, Tc) -> int | float:
    """
        Simple WACC calculator
        
        info :
            - Pudding Camp Assignment 20240307-2
            
        Args : 
            E   : 기업의 시장 가치에서의 가지가본 가치
            V   : 기업의 전체 시장 가치(자기자본 + 부채)
            Re  : 자기자본의 비용(보통주 자본비용)
            D   : 기업의 시장가치에서의 부채 가지
            Rd  : 부채의 비용(이자율)
            Tc  : 기업의 법인세율 
        
        Returns : 
            int | float : 계산 결과
            
            
        >>> calc_wacc(600000000, 400000000, 0.08, 0.05, 0.3)
        0.062
    """

    V       = Calculator(E, D).add()
    x1      = Calculator(E, V).div()
    x2      = Calculator(D, V).div() 
    x3      = Calculator(1, Tc).sub() 

    res = Calculator(x1, Re).mul() + Calculator(Calculator(x2, Rd).mul(), x3).mul()  
    
    return print(f"""The WACC of the Company is {res}.
                    - E   = {E}
                    - V   = {x1}
                    - Re  = {Re}
                    - D   = {D}
                    - Rd  = {Rd}
                    - Tc  = {x3}
                 """)
    


def test_answer() :
    assert calc_bmi(640000, 160) == 25
    assert round(calc_wacc(600000000, 400000000, 0.08, 0.05, 0.3), 3) == 0.062