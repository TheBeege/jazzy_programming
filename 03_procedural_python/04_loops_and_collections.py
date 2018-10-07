#!/usr/bin/env python3

# Now for loops! Loops are how your program can accomplish the same logic
# multiple times with little effort on your part. Let's dive in, cuz this one
# is suuuuper long. You ready?

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
# So let's demonstrate some of that mutable goodness
print('x before:', x)
x[0] = 10
print('x after:', x)
# This is how you can change a value inside a list. What about adding to a list?
x.append('added!')
print('x after adding a value:', x)
# Nice. Removing a value?
x.pop(-1)
print('x after removing the added value:', x)
# Now here's something cool
value_removed = x.pop(0)
print('value removed:', value_removed, '-- x:', x)
# Pop not only removes the value at the given index (position) from the list.
# It also returns it for use. An alternative is del:
del(x[0])
print('x after del:', x)
# This removes the value without returning it. Granted, it would only be a
# miniscule performance gain, but it's a thing.
# What about this?

y = [1, 2, 3, 4]
z = x + y
# Adding lists?!
print('z:', z)
# This... actually makes sense. Adding two lists creates a new list with the
# contents of both. Here you'll get 0, 'hi', -1, True, None, 1, 2, 3, 4.
# Magical. But what other collections are there?

x = {1, 2, 3, 3, 3, 3, 3}
print('x:', x)
# This is a set. A set allows only one of each value. All of those repeating
# 3's will simply disappear. Be aware: sets do not preserve order. The
# major purpose of sets is for handling duplicates. While we're at it, let's
# do a cool trick:

print('4 is in x?', 4 in x)
print('3 in x?', 3 in x)
# Remember when we were checking if help was in helpful? Turns out, strings
# are kind of a type of collection - they're a string of characters, a
# collection of characters. The "in" operator works for any collection.
# Now, what if I want a collection of things, but I want to keep track of
# them by name instead of by position or to just see if they exist uniquely?

x = {'key': 'value', 'bob_age': 30, 10: 'ten'}
print('x:', x)
# Notice this uses curly brackets like a set, but it's something different.
# Python calls this a dictionary - a set of key-value pairs. Take a look

print('x["key"]:', x['key'])
print('x[10]:', x[10])
# Here, 'key' and 10 are the keys in the dictionary. They are bound to the
# values 'value' and 'ten', respectively. This way, if you need to reference
# something by a name, you can do so easily. When talking about dictionaries
# with other developers, it might be helpful to know they're also called
# maps or hash tables. Maps are what they're called in languages like Java
# and Javascript. A hash table is a specific way of creating a dictionary.
# Now, what if I want to iterate through this? What if I want to access
# all of the contents?

for key in x.keys():
    print('x key:', key)

for value in x.values():
    print('x value:', value)
# Dictionaries have the methods keys() and values() to output a collection
# of the keys and values of the dictionary, respectively. Here's a neat trick

for key in x.keys():
    print('key:', key, '-- value:', x[key])
# This is a nifty way to access all the keys and values as needed. Just use the
# key to access the value. Alternatively, if you want to get super fancy...

for key, value in x.items():
    print('items - key:', key, '-- value:', value)
# I wanted to tell you both ways of doing this because I know that sometimes
# I forget this method is called items(). Now, a little bit about what's going
# on under the hood here. The items() method actually returns a tuple
# each time it's called. The first item in that tuple is the key, and the
# second item in that tuple is the value. Effectively, we're doing
# multiple assignments when doing the aboves. You can set multiple variables
# at the same time from a collection. This is called unpacking.
# Let's demonstrate in a standalone way

x, y, z = ('a', 1, True)
print('x:', x)
print('y:', y)
print('z:', z)
# Python unpacks each item in the collection, assigning it to the
# corresponding variable, in order. The items() function essentially does this.
# Let's get complicated real quick

the_big_one = {
    'some_list': [5, 10, 3.1, 22/7, True, 'lol'],
    'da_set': {False, False, False, False},
    'dict': {'key': 'val', 'name': 'Jazzimus Maximus'}
}
print('the_big_one:', the_big_one)
# Yes, you can put collections inside each other. This is _super_ useful,
# but can get really confusing, too. Let's play with this a bit

print('last in list:', the_big_one['some_list'][-1])
# When nesting (or putting one inside another) collections, you can reference
# them one by one. So using ['some_list'] pulls out the list value from
# the top-level dictionary. At that point, the list takes the place of
# the_big_one['some-list'], so we can now treat that whole thing as a list.
# By doing [-1] after that, we're accessing the last item in the list.
# In this way, you can have N-dimensional space in code. Theoretical
# physicists love this. Okay, one last thing before we're done with this

x = [2, 5, 2, 7, 10, 10]
print('list x:', x)
x = set(x)
print('set x:', x)
# This is type conversion. The variable x starts as a list. The set() function
# converts it to a set, removing duplicates. This works for all types, if
# a conversion makes sense from one type to the other

x = tuple(x)
print('tuple x:', x)
x = list(x)
print('list x:', x)
# You'll notice in the printed output that the symbols around the collection
# change to match the type of collection it is. Type conversion is useful for
#  making a tuple mutable or removing duplicates from something.

# Great job! At this point, you've covered most of the basic constructs.
# Next, we'll work on more real-world stuff, like reading files and
# downloading data from the internet
