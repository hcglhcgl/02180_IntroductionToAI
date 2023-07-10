from sympy import *
# Define two expressions
p, q, r = symbols('p q r')

# Exam 2022 last Exercise
# 3
left = Or(p, q)
right = Or(p, Not(q))
expr1 = And(left,right)
expr2 = p

# Check if the expressions are equivalent
negation = Not(Equivalent(expr1, expr2))
if not satisfiable(negation):
    print("The expressions are equivalent")
else:
    print("The expressions are not equivalent")

# Exam 2023
left = Or(p, q)
right = Or(Not(p), q)
expr1 = And(left,right)
expr2 = q

# Check if the expressions are equivalent
negation = Not(Equivalent(expr1, expr2))
if not satisfiable(negation):
    print("The expressions are equivalent")
else:
    print("The expressions are not equivalent")

