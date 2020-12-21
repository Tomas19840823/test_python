# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:11:21 2020

@author: tomas.usinskas
"""

import os
import pandas as pd

#path = os.getcwd()
os.chdir('C:/Users/tomas.usinskas/OneDrive - Scorify/Desktop')

df = pd.read_excel ('Book2.xlsx')


df.groupby("RiskGrade")["AnnualSales"].sum()

df.to_excel('./test_result1.xlsx')

