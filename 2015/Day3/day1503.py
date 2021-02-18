#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:42:10 2021

@author: houx14
"""

# Advent of Code 2015 Day 3
## Puzzle 1
import os
import pandas as pd
path = "/Users/houx14/Advent_of_Code/Advent_of_Code/2015/Day3"
os.chdir(path)
puzzle = open("input.txt", "r")
data = puzzle.read()


def find_loc(data):
    origin = [0, 0]
    pre_loc = []
    location = []

    for x in range(0,len(data)):
        if x == 0:
            pre_loc = origin
            location.append(origin)
        else:
            if data[x] == "^":
                current_loc = [pre_loc[0] + 1, pre_loc[1]]
                pre_loc = current_loc
                location.append(current_loc)
            elif data[x] == "v":
                current_loc = [pre_loc[0] - 1, pre_loc[1]]
                pre_loc = current_loc
                location.append(current_loc)
            elif data[x] == ">":
                current_loc = [pre_loc[0], pre_loc[1] + 1]
                pre_loc = current_loc
                location.append(current_loc)
            elif data[x] == "<":
                current_loc = [pre_loc[0], pre_loc[1] - 1]
                pre_loc = current_loc
                location.append(current_loc)
    return location

location_df = pd.DataFrame(find_loc(data))
n_identical_loc = len(location_df.drop_duplicates())

## Puzzle 2
data_santa = []
data_robo = []

for y in range(0, len(data), 2):
    data_santa.append(data[y])
    
for z in range(1, len(data), 2):
    data_robo.append(data[z])

santa_df = pd.DataFrame(find_loc(data_santa))
robo_df = pd.DataFrame(find_loc(data_robo))
all_location = pd.concat([santa_df, robo_df])
n_identical_loc_2 = len(all_location.drop_duplicates())
