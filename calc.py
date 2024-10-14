from library.operations import Calculator
from library.dictionary import operands
while True:
    expression=input("calc> ")
    if expression=="exit":
        break
    calcs=Calculator(0)
    calcs.parse(expression)
    print(calcs.flow)

print("bye")