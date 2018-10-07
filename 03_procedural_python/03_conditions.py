#!/usr/bin/env python3

# Now for conditions! Conditions are how programs make decisions. They're part
# of a larger set of constructs called "control flow", since they control
# the flow of the program or which code will and won't be executed
# The logic is "if this, then that" where "this" is some test of truth
# and "that" is what to do if the test is true. Let's get to it

if True:
    print('True is true')
# The test of truth is whatever is between the "if" and the colon. If whatever
# is there evaluates to true, the condition passes. If the condition passes,
# then whatever is indented beneath it will execute, until the indentation stops
# The colon is effectively the "then". So what constitutes truth?

if 5 > 10:
    print('5 is greater than 10')
# This will evaluate to false and not print. Comparison operators,
# such as <, >, <=, >=, ==, and != evaluate to either True or False
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to
# == Equal to
# != Not equal to
# Notice that == uses two equal signs. This is to distinguish between
# assignment, like with variables, and comparison, like here. In some languages
# the act of assignment can be True or False, so many languages, Python
# included, make the distinction between the two operations.
# But what if we want to do something only if a condition fails?

if 5 > 10:
    print('5 is greater than 10')
else:
    print('5 is not greater than 10')
# "Else" is similar to "if" in that it controls whether code is run. If the
# immediately preceding condition passes the truth test, then the indented
# content below else (also called, the code block for else) is not executed.
# If the preceding condition(s) fail, then the else is run. In the case above,
# '5 is not greater than 10' will be printed, since the test for 5 > 10 does
# not evaluate to True

if 5 > 10:
    print('5 is greater than 10')
elif 10 == 10:
    print('10 is equal to 10')
else:
    print('Neither 5 is greater than 10 nor is 10 equal to 10')
# The elif bit is unique to Python. It's a combination of else and if. Like
# if, it also does a test of truth, but like else, it will only run if all
# preceding conditions in the same block do not pass their tests of truth.
# So in the case above, 5 > 10 fails, so the program continues in the block.
# Following this, it sees the elif and checks the condition. Ends up that
# 10 == 10 passes the test of truth. The elif's code block is executed, and
# all remaining elses in this code block are ignored. This can get complicated,
# but it does allow you to create complex logic.

if 5 > 10:
    print('5 is greater than 10')
elif 10 == 10:
    print('10 is equal to 10 once')
elif 10 == 10:
    print('10 is equal to 10 twice')
elif 10 == 10:
    print('10 is equal to 10 thrice')
else:
    print('Neither 5 is greater than 10 nor is 10 equal to 10')
# What do you think will be printed?


# The only thing printed will be '10 is equal to 10 once'. The first condition
# fails the test of truth, and since the 'once' block is the first once that
# passes, all of the remaining ones are ignored.


if 5 > 10:
    print('5 is greater than 10')
elif 10 == 10:
    print('10 is equal to 10 once')
elif 10 == 10:
    print('10 is equal to 10 twice')
if 10 == 10:
    print('10 is equal to 10 thrice')
else:
    print('Neither 5 is greater than 10 nor is 10 equal to 10')
# How about this one? What will be printed?

# The once and thrice prints will show up. Since the if of thrice starts a
# new condition block, the previous conditions don't play into this condition's
# decision. This can get complicated. Normally, for readability, you would
# add an extra newline in between the two condition blocks to make it easier
# to distinguish for your future self. Now, is everything only comparisons?

if 'help' in 'helpful':
    print('help is a part of helpful')
# There are other operations that evaluate to True or False. Here we have the
# "in" operator, which checks to see, in this case, if one string is within
# another. The above evalutes to True, and the text runs. What about other,
# more unusual cases?

if None:
    print('None is true')
else:
    print('None is false')
# In Python, almost everything evaluates to either True or False. Here, we have
# the construct "None". None represents a lack of information. As such, the
# creators of Python decided it should evaluate to False when being tested
# for truth. As such, 'None is false' is printed. What about more cases?

if 'hello' == 'goodbye':
    print('hello is equal to goodbye')
elif 'hello' == 'hello':
    print('hello is equal to hello')
else:
    print('hello is not equal to goodbye or hello')
# We can also compare strings of text. The only valuable comparisons are
# equality and inequality. Less than and greater than do work, but
# they're not easily read and should be avoided. I don't even know how their
# comparisons work. Can we get fancier with comparisons?

if len('aaaa') == len('bbbb'):
    print('The length of aaaa is equal to the length of bbbb')
# We can always get fancier. Everything evaluates somehow. Above, we're using
# the len() or length function on strings. These are evaluated before the
# comparison takes place. The final comparison ends up being 4 == 4. You
# could do this with any function and any value. Just make sure to not go
# overboard and to keep things readable. Now, what if we wanted more
# complicated logic?

if True and False:
    print('Both true and false are true')
elif True or False:
    print('Either true or false is true')
# We can always get more complicated, too. The best way to explain how this
# works is to show a truth table, which you can also find on the internet by
# that name.
# _________________________________________________
# |  First   |  Second   | and result | or result |
# |  True    |   True    |  True      |   True    |
# |  True    |   False   |  False     |   True    |
# |  False   |   True    |  False     |   True    |
# |  False   |   False   |  False     |   False   |
# For the "and" operator, the values on both sides of it must be True, or
# it will evaluate to False. For the "or" operator, if either side evaluates
# to True, it will evaluate to True. If both sides are False, it evaluates
# to False. Python does not have the XOR and NAND operators. If you need these,
# you can accomplish them with comparisons, parenthesis, and not. See below

if not (10 < 5) and not (5 > 10):
    print("Poor man's NAND")
# Yeah, this is gross. NAND is only true if both inputs are false. To
# accomplish this without NAND, we test two conditions for being False.
# We do this by taking either side, wrapping it in parenthesis to group it,
# and appling a not to invert the result. To go through it in detail,
# 10 is not less than 5, so it evaluates to False. The not is then applied to
# it, turning it from False to true. We do the same with the other side of the
# and. We end up with True on both sides, making our and evaluate to True.
# This gives us our NAND operation - it is only True if both sides are False

if 5 == 5 and not (1 == 5):
    print("Poor man's XOR")
# XOR is only true if one input is True and the other is False. We can do this
# by using an and with a not on one side. It's not quite as robust as a true
# XOR, since we have to be specific as to which side is True and which side is
# False, but a real XOR would be much more complicated

# This is one of the more complicated early topics, but you got through it!
# Good job! Maybe take some time to experiment with your own conditions to
# make sure you've got it~
