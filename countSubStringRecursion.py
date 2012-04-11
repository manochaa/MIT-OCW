#-------------------------------------------------------------------------------
# Name:        countSubStringRecursion
# Purpose:      Finds and prints a list of positions where a sub string is found
#               in a larger string.
#
# Author:      Ayush Manocha
#
# Created:     30/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

from string import *

def countSubStringRecursion(target, key, startPoint = 0):
    index = find(target,key, startPoint)
    if index >= 0:
        return countSubStringRecursion(target,key, index+1)+1
    return 0
