>Note - If you don't want to pop changed variable after backtracking call is returned simple change the variable in func call itself.
for Ex -
See generate parenthesis code.

1.
stack.append(")")
backtracking(open, closed+1) # last time when execution of this line is done, stack will look like [( ( ( ) ) )], and when last time execution of this line is done it prints.  This line was called by bactracking (3, 2)
stack.pop()

2.
self.generate(stack + ["("], left - 1, right, result)

It works because when you get back the control to the calling function, the stack value is still the same.
You are changing it only for the called function i.e in its parameter.

