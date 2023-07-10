from sympy import *

def implies(S, x):
    S = [to_cnf(s) for s in S]
    print(S)
    x = to_cnf(x)
    return not satisfiable(And(*S, Not(x)))

# Example usage
p, q, r= symbols('p q r')
beliefs = [q, p, And(p, Not(q))]
element = Or(p,Not(p))

# Check if ~p is in beliefs
if implies(beliefs, element):
    print(f"{element} is a logical consequence of beliefs")
else:
    print(f"{element} is not a logical consequence of beliefs")


# Check if the sentence can be derived from the belief base
result = satisfiable(And(*beliefs, Not(element)))

if result:
    print(f"{element} cannot be derived from the belief base")
else:
    print(f"{element} can be derived from the belief base")