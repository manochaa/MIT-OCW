#-------------------------------------------------------------------------------
# Name:        p4a.py
# Purpose:  Retirement planning
#
# Author:      cain297
#
# Created:     10/04/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

import math

def nestEggFixed(salary, save, growthRate, years):
    total = 0
    totalListed = []
    for i in range(years+1):
        total += (total * (1+growthRate))+ (save*salary*growthRate)
        totalListed.append(total)
    return totalListed

print nestEggFixed(10000,.10,.15,5)