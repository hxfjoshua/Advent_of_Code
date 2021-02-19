#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:54:25 2021

@author: Xuefeng Hou

URL: https://adventofcode.com/2015/day/4
"""

# Puzzle 1
# Goal is to find the number that follows the given key, convert this hexadecimal to MD5 hash
import hashlib
key = "bgvyzdsv"
N = 5 #first N digits are zeros as required
num = 1
hex_string = key + str(num)
while hashlib.md5(hex_string.encode()).hexdigest()[0:N] != "00000":
    num += 1
    hex_string = key + str(num)
    if hashlib.md5(hex_string.encode()).hexdigest()[0:N] == "00000":
        print(str(num))
        break

# Puzzle 2
N = 6
num = 1
hex_string = key + str(num)
while hashlib.md5(hex_string.encode()).hexdigest()[0:N] != "000000":
    num += 1
    hex_string = key + str(num)
    if hashlib.md5(hex_string.encode()).hexdigest()[0:N] == "000000":
        print(str(num))
        break