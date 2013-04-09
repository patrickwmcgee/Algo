#!/usr/bin/python

import insertion_asc
import insertion_desc
import merge
a = [100,30,40,50,22,8,13,4,7,9,10,15]
b = [0,30,40,50,22,8,13,4,7,9,10,15]
c = [30,12,15,2,68,96,42,71]
print 'asc'
print 'before'
print a # print before sort
insertion_asc.insertion_sort_asc(a)
print 'after'
print a # print after sort

print 'desc'
print 'before'
print b # print before sort
insertion_desc.insertion_sort_desc(b)
print 'after'
print b # print after sort

print 'merge'
print c
merge.merge_sort(c,1,len(c))
print c