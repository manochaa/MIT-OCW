#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cain297
#
# Created:     20/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

n = int(raw_input("Please enter the combination that you'd like to find"))
a = int((n/20))+1
bc = int((n/9))+1
cc = int((n/6))+1

for i in range(0,a):
#    print i
    for j in range(0,bc):
#           print j
            for k in range(0,cc):
                if (6*k+9*j+20*i) == n:
                    print "The combination is", k,j,i
