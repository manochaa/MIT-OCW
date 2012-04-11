#-------------------------------------------------------------------------------
# Name:        Ayush Manocha
# Purpose:      Find the positions where a key word appears in a target string.
#
# Author:      cain297
#
# Created:     27/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

from string import *



def countSubString(target,key):
    count = []
    aa = 0
    lenT = len(target)
    while aa <= lenT:
        l = target.find(key,aa)
        if l != -1:
            aa = l+1
            count.append(l)
        else:
            aa += 1

    print count