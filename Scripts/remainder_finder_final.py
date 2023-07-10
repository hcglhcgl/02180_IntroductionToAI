from sympy import *

def is_subset(S, A):
    return S.issubset(A)

def implies(S, x):
    S = [to_cnf(s) for s in S]
    x = to_cnf(x)
    return not satisfiable(And(*S) & Not(x))

def filter_subsets(sets):
    filtered_sets = []
    for s in sets:
        if not any(s.issubset(other) for other in sets if s != other):
            filtered_sets.append(s)
    return filtered_sets

def check(A,x,sets_to_check):
    # Check if each set is a subset of A
    print("Checking if each set is a subset of A")
    for S in sets_to_check:
        if is_subset(S, A):
            print(f"True: {S} is a subset of {A}")
        else:
            print(f"False: {S} is not a subset of {A}")
    print("------------------------------------------------------------")
    # Check if each set implies x
    print("Checking if each set implies x")
    for S in sets_to_check:
        if implies(S, x):
            print(f"True: {S} implies {x}")
        else:
            print(f"False: {S} does not imply {x}")
            
    # Print a list of the elements that are subsets and do NOT imply x
    good_sets=[]
    print("------------------------------------------------------------")
    print("The following sets are subsets of A and do not imply x:")
    for S in sets_to_check:
        if is_subset(S, A) and not implies(S, x):
            print(f"{S} is a subset of {A} and does not imply {x}")
            good_sets.append(S)
    print("------------------------------------------------------------")
    print("Now we will filter out the sets which are already subsets of others, giving us the the final result:")
    filtered_sets = filter_subsets(good_sets)
    for set in filtered_sets:
        print(set)
        print(pretty(set))
        
# Practice Exam 2023
print("Practice Exam 2023")
# Define the belief base A and the set S
p, q = symbols('p q')
A = [p, q, Implies(p, q), Implies(Not(p), q)]
x = q

sets_to_check = [
    {p, q, Implies(p, q), Implies(Not(p), q)},
    {p, q},
    {p},
    {q},
    {p, q, Implies(p, q)},
    {p, q, Implies(Not(p), q)},
    {p, Implies(Not(p), q)},
    {p, Implies(p, q)},
    {q, Implies(p, q)},
    {q, Implies(Not(p), q)},
    {Implies(p, q), Implies(Not(p), q)},
    {Implies(p,q)},
    {Implies(Not(p),q)},
    {q, Implies(p,q), Implies(Not(p),q)},
    {p, Implies(p,q), Implies(Not(p),q)}
]

check(A,x,sets_to_check)

# Exam 2022
print("#####################################################")
print("Exam 2022")
p, q = symbols('p q')
A = [p, q, Or(p,q), Implies(p, q), Implies(Not(p), q)]
x = q

sets_to_check = [
    {p, Not(q),Or(p,q),Implies(Not(p), q)},
    {p,Or(p,q),Implies(p, q),Implies(Not(p), q)},
    {p,Or(p,q),Implies(Not(p), q)},
    {p,Or(p,q)},
    {Or(p,q),Implies(p, q),Implies(Not(p), q)}
]

check(A,x,sets_to_check)

# Week 12, Exercercise 2
print("#####################################################")
print("Week 12, Exercercise 2")
p, q = symbols('p q')
A = [p, q, Or(p,q), Implies(p, q), Implies(Not(p), q)]
x = q

sets_to_check = [
    {p,Or(p,q)},
    {Implies(p, q)},
    {Or(p,q),Implies(p, q)},
    {Or(p,q)}
]

check(A,x,sets_to_check)

# Lecture 11 Example
print("#####################################################")
print("Lecture 11 Example")
p, q = symbols('p q')
A = [p, And(p,q), Or(p,q), Equivalent(p, q)]
x = p

sets_to_check = [
    {Or(p,q)},
    {Equivalent(p, q)}
]

check(A,x,sets_to_check)

# Exam 2019 Example
print("#####################################################")
print("Exam 2019")
p, q = symbols('p q')
A = [p,q, And(p,q), Or(p,q), Implies(p, q)]
x = q

sets_to_check = [
    {p,Or(p,q)},
    {Implies(p, q)},
    {Or(p,q),Implies(p, q)},
    {Or(p,q)}    
]

check(A,x,sets_to_check)

# Exam 2023 Example
print("#####################################################")
print("Exam 2023")
p, q = symbols('p q')
A = [p,q, Not(And(Not(p),Not(q))), Implies(p, q),Implies(Not(p), q)]
x = q

sets_to_check = [
    {p,Not(q),Or(p,q),Implies(Not(p), q)},
    {p,Not(And(Not(p),Not(q)))},
    {p,Not(And(Not(p),Not(q))),Implies(p, q),Implies(Not(p), q)},
    {Not(And(Not(p),Not(q))),Implies(p, q),Implies(Not(p), q)},
    {p,Not(And(Not(p),Not(q))),Implies(Not(p), q)}    
]

check(A,x,sets_to_check)