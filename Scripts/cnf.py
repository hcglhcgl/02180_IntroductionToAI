from sympy import *

p, q, r, s = symbols('p q r s')
expr1 = Or(p, q, r)
expr2 = Or(Not(r),q)

result = to_cnf(And(expr1, expr2))
print(result)

expr1 = Implies(And(p,s),r)

result = to_cnf(expr1)
print(result)

left = Or(Not(p),q)
right = Or(Not(q),p)
expr1 = Or(left,right)

result = to_dnf(expr1)
print(result)