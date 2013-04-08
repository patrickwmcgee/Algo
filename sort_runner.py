#!/usr/bin/python

import insertion_asc

a = [30,40,50,22,8,13,4,7,9,10,15]
b = a
c = a

print a # print before sort
insertion_asc.insertion_sort_asc(a)
print a # print after sort