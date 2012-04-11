#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cain297
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

def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])