#!/usr/bin/env python

from sender import Sender as s

sender = [s(0,0,5), s(0,10,6), s(5,5,3), s(10,5,3), s(10,15,1)]

for elem in sender:
    elem.refresh_overlap(sender)
    print elem

print "TEST"
