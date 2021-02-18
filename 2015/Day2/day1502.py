#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:37:04 2021

@author: Xuefeng Hou
"""

# Advent of Code 2015 Day 2
## Puzzle 1
import os
import pandas as pd
path = "/Users/houx14/Advent_of_Code/Advent_of_Code/2015/Day2"
os.chdir(path)
puzzle = open("input.txt", "r")
data = puzzle.read()
#type(data)

data = data.split('\n')

# Define function to split by 'x', and rearrange the dimension in ascending orders
def new_order(data):
    data_split = data.split('x')
    data_intgr = [int(x) for x in data_split]
    reorder = sorted(data_intgr)
    return reorder

data_new = [new_order(x) for x in data]

data_df = pd.DataFrame(data_new)
data_df.columns = ['L', 'W', 'H']

total_area = 3 * (data_df['L'] * data_df['W']) + 2 * (data_df['L'] * data_df['H'] + data_df['W'] * data_df['H'])
total_area.sum()

## Puzzle 2
total_ribbon = 2 * (data_df['L'] + data_df['W']) + (data_df['L'] * data_df['W'] * data_df['H'])
total_ribbon.sum()
