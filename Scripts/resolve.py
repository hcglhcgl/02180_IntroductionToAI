from sympy import *
from sympy.logic.boolalg import Or, Not

def resolve(clause1, clause2):
    for literal in clause1.args:
        if Not(literal) in clause2.args:
            new_args = [x for x in clause1.args if x != literal] + [x for x in clause2.args if x != Not(literal)]
            return Or(*new_args)
    return None

# Example usage
p, q, r = symbols('p q r')
clause1 = Or(p,q,r)
clause2 = Or(Not(r),p)

resolvent = resolve(clause1, clause2)
print("Resolvent:", resolvent)