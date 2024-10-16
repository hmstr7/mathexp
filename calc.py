from mathexp.operations import Calculator
calcs=Calculator(0)
while True:
    calcs.reset() # Set the internal value of calculator to initial value given when cre+[]ating object.
    expression=input("calc> ")
    if expression=="exit":
        break
    calcs.parse(expression) # Give a string expression to the calculator, so it'll parse it and change its 'flow' value.
    print(calcs.flow)
print("bye")