#!/usr/bin/env python3

# Now for loops! Loops are how your program can accomplish the same logic
# multiple times with little effort on your part. Let's dive in

for i in range(10):
    print('i is: ', i)
# There's actually a lot going on here, so let's finally break it down.
# The "for" indicates to Python that we're starting a loop. Following for,
# we have our iterating variable. The iterating variable is the name for
# the variable that will store the information changing for each step of
# the loop. Following the iterating variable is the keyword "in", which
# tells Python that some sort of collection is coming next. The collection is
# a number of some values all grouped into one sort of structure. We'll get
# into collections in greater detail in a short bit. After the collection is a
# colon, followed by the indented code that will be repeated until no items
# are left in the collection. For each execution of the loop, the iterating
# variable will be set to a value from the collection, in order.
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
# Let's unpack this. In this example, instead of using a range function for our
# collection, we have something called a tuple. A tuple is a group of values
# in some order, and it is immutable - it cannot be changed. In this example,
# i will first be set to 9, then the loop's block will be executed. Next,
# i will be set to 3, and the block will execute again. This finishes with 11,
# after which point the loop stops, and the program continues going down.
# One key thing about a tuple is that it cannot be changed. Why is this useful?
# It's a way to communicate with the developer. Here's an example. Say you're
# writing a database library. To change data in the database, you need to
# connect to the database, send a request for the data you want to get,
# receive the response, parse the response, and format it in a way to be used.
# To change the data in the database requires a similar level of effort.
# When you give data to the programmer from the database, you probably want
# to give them a tuple. This is because you want to communicate to the
# developer that simply changing the data in this collection will not change
# what's in the database. You have to go through some large operation to do
# that. By preventing the developer from changing the data you give them,
# you communicate this very clearly, forcing them to do the extra work
# if they want to change the value in the database.
# But enough on that, how else can you use a tuple?

x = (5, 8, 3, 6, 0, 3, -1)
# What if I only want the second value from the tuple?
print('second value in tuple x:', x[1])
# But dude, I want the second value. Why the hell did you write 1?
# We count from 0 in programming, remember? When working with a tuple, you
# can put square brackets after it surrounding a number to indicate which
# value you want out o the tuple. Fancy, right?
# What if I only want to print the second through fifth values?

for i in x[1:5]:
    print('i as the second through fifth values of x:', i)
# You can use a colon inside the square brackets to denote which values you
# want to go through. This effectively creates a new tuple as (8, 3, 6, 0) and
# loops through it. What if we want all but the first value?

for i in x[1:]:
    print('i as all but the first of x:', i)
# If you leave off the second value after the colon, it will just go to the end.
# But what about all but the last?

for i in x[:-1]:
    print('i as all but the last of x:', i)
# Not bad. What if I told you that this was kind of like range?

for i in x[::-1]:
    print('i as all of x but backwards:', i)
# Mind. Blown. Leave out the first value, and it goes to the end. Leave out the
# second value, and it goes to the end. You can have a second colon with a
# third value to specify how you should step, just like range. Pretty nifty.
# But hey, tuples aren't the only type of collection. Let's check out more

x = [5, 2, 0, 'hi', -1, True, None]
# This is a list. It's ordered, like a tuple. Unlike a tuple, it uses
# square brackets [] to denote itself and is mutable - you can change it.
# Tuples can also store different types of values, but I wasn't thinking
# about that before.
