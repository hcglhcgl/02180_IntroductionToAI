from sympy import *
from sympy.logic.inference import satisfiable
p, q, r = symbols('p q r')
# Define the belief base and the sentence to check
# Exam 2022 opg 2
beliefs = [q, And(p, Not(q))]
sentence = Not(p)
beliefs = [q, p, And(p, Not(q))]
sentence = Or(p,Not(p))
# Check if the sentence can be derived from the belief base
result = satisfiable(And(*beliefs, Not(sentence)))

if result:
    print(f"{sentence} cannot be derived from the belief base")
else:
    print(f"{sentence} can be derived from the belief base")