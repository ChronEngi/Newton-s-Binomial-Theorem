### By ChronEngi on GitHub ###

import math
from colorama import Fore, Back, Style
import os

while True:

    os.system("cls")
    output = ""

    print("Newton's Binomial Theorem\n")
    print("(x + y)^n\n")

    n = int(input("n = "))

    if n > 1029:
        print("\nSorry the max is 1029.")
        os.system("pause");
        exit(1)

    print(f"\n(x + y)^{n} = ∑^n (n/k)*x^(n-k)*y^k\n")

    for k in range(n + 1):
        term = ""

        # Compute the binomial coefficient
        ans_nominatore_coefficente = math.factorial(n)
        ans_denominatore_coefficente = math.factorial(k) * math.factorial(n - k)
        coefficente = int(ans_nominatore_coefficente / ans_denominatore_coefficente)

        # Add the coefficient if it's not 1 (don't show 1 as a coefficient)
        if coefficente != 1:
            term = str(coefficente)

        # Add x^(n-k) only if n-k is not 0, and don't show x^1 as x^1, just x
        if (n - k) != 0:
            term += "x"
            if (n - k) != 1:
                term += f"^{n - k}"

        # Add y^k only if k is not 0, and don't show y^1 as y^1, just y
        if k != 0:
            term += "y"
            if k != 1:
                term += f"^{k}"

        if k == n:
            output += term + " "
        else:
            output += term + " + "

        print(term)
        print("\n----\n")

    # Final output
    print("\nFinal expression: (x + y)^"+ str(n) + " = " + Fore.LIGHTGREEN_EX + output + Fore.RESET)
    print("\nPress ENTER to continue.")
    input()