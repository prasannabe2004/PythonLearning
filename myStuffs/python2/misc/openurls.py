# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:30:26 2015

@author: pmohanasundaram
"""

import webbrowser


f1 = open("urls.txt")
for i in f1:
    print i
    webbrowser.open(i)
    
f1.close()