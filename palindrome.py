#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
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

worD = str(raw_input("Please enter the string"))

def isPalindrome(x):
    if len(x) <= 1:
        return True
    else:
        return x[0] == x[-1] and isPalindrome(x[1:-1])
    return False

print isPalindrome(worD)
