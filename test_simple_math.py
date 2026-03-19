#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:34:19 2026

@author: geoffreydesena
"""

# test_simple_math.py

import simple_math

def test_simple_add():
    assert simple_math.simple_add(1, 1) == 2
    
def test_simple_sub():
    assert simple_math.simple_sub(10,9) == 1
    
def test_simple_mult():
    assert simple_math.simple_mult(3,4) == 12
    
def test_simple_div():
    assert simple_math.simple_div(10,2) == 5
    
def test_poly_first():
    assert simple_math.poly_first(3, 1, 2) == 7
    
def test_poly_second():
    assert simple_math.poly_second(3, 1, 2, 0) == 7 
    
