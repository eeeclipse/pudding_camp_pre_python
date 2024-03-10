#! /usr/bin/env python

import pytest 
from src.calc_class import Calculator


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
    


def test_answer():
    assert calc_bmi(64000, 160) == 25
