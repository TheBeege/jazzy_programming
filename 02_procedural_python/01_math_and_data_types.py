#!/usr/bin/env python3

# This might be old news to you, as much of things so far has been, but it may be a nice refresher. Let's run through it.

print("hi")
# This is the print() function. It prints stuff out to terminal. Pretty simple, right?

print("hi", "there")
# The print function takes multiple arguments (also called parameters). These arguments go between the parenthesis (). Each argument is separated by a comma. For print, a space is put between each argument. You could just type "hi there", but I just wanted to demonstrate how this worked.

x = 5
# This is a variable. We've created a variable called "x", and we've set its initial value to 5. This value can change. When referenced, the value of the variable is used. What does that mean?

print("x is", x)
# This means that 5 will take the place of the x outside quotations here. When there is text inside either single or double quotation marks, it is treated as text data. We call this a string. Why? Each letter/number/punctuation/etc is called a character. A string is a sequence (or string) of characters put together. If there is text outside of quotations, Python attempts to treat it as code. In this case, it sees x outside of quotations, so it looks for either a variable or function called x. It finds the variable we defined above, and it substitutes the value of the variable into the print function.

# We can also modify variables.
x = x + 1
print("added 1 to x:", x)
# You'll see that x is now 6. In line 18, we set the new value of x to the existing value of x plus one. Some people find this remarkably difficult to understand at first. Just remembered that when we're doing assignment (or setting the value of things), whatever is right of the equals sign happens first. In this case, x + 1 is evaluated to 5 + 1, which then becomes 6. Then x is set to 6.

# We can also be a liiiiittle lazier
x += 1
print("added 1 more to x:", x)
# Line 23 is the same as line 18, just written differently.

# You can also subtract
x -= 1
print("removed 1 from x:", x)

# You can multiply
x *= 2
print("multiplied x by 2:", x)

# You can also divide
x /= 2
print("divided x by 2:", x)
# You'll notice that x now appears as 6.0 instead of 6. We'll cover why in a minute

# You can also floor divide, which cuts off any non-whole-number amount
print("x floor divided by 4:", x // 4)

# There's also the modulo operator, which will give you the remainder of a division operation
print("x modulo 4:", x % 4)

# Okay, now why did dividing give us 6.0 instead of 6? This is due to the concept of data types. Python tries to make things such that you don't need to worry about data types, but there really is no escaping it. Initially, x is an integer - a whole number. However, the division operation does not produce an integer. It produces a floating point number, or a decimal. Normally, I'd skip what floating point means, but if you're doing number crunching, it's important to know. Let's say we have a number like this: 436,312,683,904,124,673. Big number. The computer doesn't have unlimited data. It has limited amounts of data it can store, and it wants to be efficient. Representing that number in binary would be quite large. Similar to laboratory sciences, we use approximations. In lab science, we might represent this number as 4.36312 x 10^16. We cut off the remaining numbers because they're not significant with respect to the size of this number. Computers do similar things. A computer only wants to use so much data to represent numbers, so it will only store the most significant digits and a reference of where the decimal (or point) is located. In this method, the point can float or move around depending on the size of the number. Hence, we call this a floating point number. This is the default way to represent decimals in Python. Since division may not return a whole number, it outputs a floating point in all cases for purposes of consistency. Other mathematical operations return the same data type as whatever was input. The reason for this is that your code likely doesn't expect data to change type terribly often. Division is kind of a special case in this regard.

# So how do we get it back to an integer?
print("x back as an integer:", int(x))
# Integer in python is referenced as int. There is an int function that takes whatever the input is and converts it to an integer, if possible. Similar functions exist for float and str (string). Play with these and see what you get.
