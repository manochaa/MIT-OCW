#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      cain297
#
# Created:     19/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def is_prime(x):
    i = 2
    while i < x**.5:
        if x%i == 0:
            return False
        i += 1
    return True


y = int(input("Please enter which prime number you'd like"))

n = 1
pcount = 1

while pcount<y:
    n += 2
    if is_prime(n):
        pcount += 1

if n == 1:
    print (2)
else:
    print(n)
