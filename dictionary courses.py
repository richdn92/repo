# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:59:44 2019

@author: richa
"""

coursesDict = {"CIS2200":{'11-103':'Jain'},"CIS3100":{'12-160':'Croker'},'CIS3120':{'12-140':'Kumar'}}

courseName = str(input('enter course: '))

#print(coursesDict[courseName])
course= coursesDict.get(courseName,"Course Not available")     

print(course)