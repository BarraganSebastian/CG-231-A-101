# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


numEl=int(input("ingrese el numero de elementos"))
numl = []

for i in range(0, numEl):
    a=int(input())
    numl.append(a)
numl.sort()
print(numl)
