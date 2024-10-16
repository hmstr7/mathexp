# mathexp
Useless and overengineered calculator written in python. Uses custom math expression form that allows some simple actions.
## How to use
Mathexp parses simple expressions that are written strictly following specific form, for example:

    +[1,1,]*[2,2,]
    This expression outputs 8. It can be interpreted as "(0+(1+1))*2*2" or "multiply(add(1,1),2,2)"
  You can use a...b to mark range between a and b:
  

    +[1,]+[1...10,]
    Outputs 46
   Also it is possible to use expressions within expressions with brackets ():
   

    +[1,]*[(+[(+[1,2,]),(+[1,]*[6,]/[2,]),]),]
    Outputs 6.0
  
  Note that calc.py uses 0 as the initial value (that is why all the examples start with +).

## Installing
There isn`t much to say, this is just your usual python script. You can use it as a library (class Calculator from mathexp/operations.py), or just run calc.py. That's all.