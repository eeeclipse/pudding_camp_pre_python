#! /usr/bin/env python

import pytest 

class Calculator :
    """
        Simple Calculator 
        
        Info :
            - Pudding Camp practice 20240307-1-2-7
    """
    
    a = 3
    b = 10 
    
    @classmethod
    def add(cls) :
        return cls.a + cls.b
    
    @classmethod
    def sub(cls) :
        return cls.a - cls.b

    @classmethod
    def mul(cls) :
        return cls.a * cls.b
    
    @classmethod
    def div(cls) :
        return cls.a / cls.b