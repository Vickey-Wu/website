#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2018/3/4 22:26 
# @name: tmp
# @author：vickey-wu


a = [1, 5, 6]
b = [2, 3, 5, 6, 8]
c = []
for i in b:
    for j in a:
        if i == j:
            c.append(i)
            break
print(c)