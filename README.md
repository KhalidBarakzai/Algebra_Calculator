# algebra_calculator

It’s possible to solve an equation numerically, by substituting numbers for its variables.
It’s also possible to solve an equation symbolically, by using algebra. For example, to solve
the equation m × x + b = y symbolically for x, you’d first subtract b from both sides, giving
m × x = y − b. Then you’d divide both sides by m, giving x = (y − b) / m. You may assume
that no variable is equal to zero.

This program uses algebra to solve simple equations symbolically. It uses Python tuples to represent equations,
and Python strings to represent variables. To simplify the code, the equations will use
only the binary arithmetic operators ‘+’, ‘−’, ‘×’, and ‘/’. Also, this version only
solves for a variable that appears exactly once in an equation.
