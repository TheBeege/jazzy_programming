#!/usr/bin/env python3

# Now for loops! Loops are how your program can accomplish the same logic
# multiple times with little effort on your part. Let's dive right in

for i in range(10):
    print('i is: ', i)
# This will print 'i is: 0' followed by 'i is: 1' followed by 'i is: 2' all
# the way up to 'i is: 9'. Range is a function that spits out of a list of
# numbers from 0 up to and excluding the given number. Why? In programming,
# we count from 0. Counting from 0 to 9 gives us 10 total numbers.
# What else can range do?

for j in range(15, 20):
    print('j is: ', j)
# Note: I used j to make the print output easier to discern. You could just
# use i again without any problems.
# This will print 15 through 19. When providing two parameters to the range
# funciton, it will print the first parameter up to and excluding the second
# parameter. It can do more, as well

for i in range(25, 20, -1):
    print('i is: ', i)
# If you give a third parameter to range, it will count by that number between
# the first two parameters. In this case, we start with 25, and we count
# down to and excluding 20 going by -1 at a time. So this will print the
# numbers 25, 24, 23, 22, 21 in that order. Let's do one more example

for j in range(50, 100, 10):
    print('j is', j)
# THis will count by 10 from 50 up to and excluding 100. This is useful for
# doing the same operation over and over again. But how does it actually
# work under the hood? Let's bring a collection into the mix, and we
# can demonstrate that

for i in (9, 3, 17, 10, 11):
    print('i is', i)
# There's actually a lot going on here, so let's break it down.
#
