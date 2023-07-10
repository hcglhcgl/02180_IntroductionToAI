from sympy.logic.boolalg import Or, And, Not
from sympy.abc import p, q

def check_formula(formula):
    if isinstance(formula, Or):
        print("The formula is a disjunction.")
        all_horn = True
        all_definite = True
        for arg in formula.args:
            positive_literals = 0
            if isinstance(arg, Or):
                for sub_arg in arg.args:
                    if not isinstance(sub_arg, Not):
                        positive_literals += 1
            elif not isinstance(arg, Not):
                positive_literals += 1
            if positive_literals > 1:
                all_horn = False
            if positive_literals != 1:
                all_definite = False
        if all_horn:
            print("The formula is a disjunction of Horn clauses.")
        elif all_definite:
            print("The formula is a disjunction of definite clauses.")
        else:
            print("The formula is a disjunction of mixed clauses.")
    elif isinstance(formula, And):
        print("The formula is a conjunction.")
        all_horn = True
        all_definite = True
        for arg in formula.args:
            positive_literals = 0
            if isinstance(arg, And):
                for sub_arg in arg.args:
                    if not isinstance(sub_arg, Not):
                        positive_literals += 1
            elif not isinstance(arg, Not):
                positive_literals += 1
            if positive_literals > 1:
                all_horn = False
            if positive_literals != 1:
                all_definite = False
        if all_horn:
            print("The formula is a conjunction of Horn clauses.")
        elif all_definite:
            print("The formula is a conjunction of definite clauses.")
        else:
            print("The formula is a conjunction of mixed clauses.")
    else:
        print("The formula is neither a conjunction nor a disjunction.")

formula = Or(Or(Not(p), q),Or(Not(q), p))
check_formula(formula)
