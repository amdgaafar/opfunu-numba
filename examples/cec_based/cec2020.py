#!/usr/bin/env python
# Created by "Thieu" at 21:33, 12/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import opfunu
import numpy as np


## Test CEC2020 F1
print("====================F1")
problem = opfunu.cec_based.F12020(ndim=30)
x = np.ones(30)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2020 F2
print("====================F2")
problem = opfunu.cec_based.F22020(ndim=30)
x = np.ones(30)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))


## Test CEC2020 F3
print("====================F3")
problem = opfunu.cec_based.F32020(ndim=30)
x = np.ones(30)
print(problem.evaluate(x))
print(problem.x_global)

print(problem.evaluate(problem.x_global))
print(problem.is_succeed(x))
print(problem.is_succeed(problem.x_global))





