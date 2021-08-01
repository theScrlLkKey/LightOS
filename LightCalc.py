# imports here
from fractions import Fraction
from sympy import symbols, solve

# defs here

# defaults here
vr = 'res = '
res = 0
ans = 0
x, y = symbols('x y')
# main here
if __name__ == "__main__":
    while True:
        print("""1: Simplify
2: Find x 
3: Equate""")
        op = input('Number: ')
        eq = input('Equation: ')
        if op == '1':
            numr, denm = eq.split('/')
            ans = Fraction(int(numr), int(denm))
        elif op == '2':
            ans = solve(eq, dict=True)
        elif op == '3':
            ans = eval(eq)
        print(ans)

