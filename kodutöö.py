#!/usr/bin/python
# coding: latin-1
import os
import random 
clear = os.system('clear');

q= 4
d= 8

while q <= d:
	print '#' * random.randint(10,40)
	q = q + 1
