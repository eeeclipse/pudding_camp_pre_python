#! /usr/bin/env python

import pytest 

class Calculator :
    """
        Simple Calculator 
        
        Info :
            - Pudding Camp practice 20240307-1-2-6
    """
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    
    def add(self) :
        return self.a + self.b
        
    def sub(self) :
        return self.a - self.b
    
    def mul(self) :
        return self.a * self.b
    
    def div(self) :
        return self.a / self.b
    
    def __str__(self) :
        return f"""a:{self.a},  b:{self.b}"""
        