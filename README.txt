CPSC 323 - Angel Villa

This is a predictive parser that uses stack implementation as well as a character ahead to
predict using the input string. There is a set of production rules given, and those are
implemented using left recursion. LL(1) stands for left recursion, from left to right,
and reading 1 symbol ahead, hence why it's a predictive parser.

This is implemented using Python, and we can enter whichever input strings we want
separated by a comma. Then it'll show each step of the way, with the stack each step,
and what production rules are being used at every step.

To run this, you simply put it into a PyCharm IDE and run whichever input string you'd
like to see in steps.