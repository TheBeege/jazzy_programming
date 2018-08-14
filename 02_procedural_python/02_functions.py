#!/usr/bin/env python3

# Let's get into functions! Functions are basically reusable bodies of code that are aliased into a single name. That may not mean much now, but hopefully it'll make sense by the end.

def print_hello():
    print("Well, hello there, you amazing thing you!")
# This is a pretty useless function, but it's a good start. This is called a function definition. It's important to know the difference between a function definition and a function invokation (or execution). We'll cover the difference shortly. Just know that this is a definition. The giveaway is the "def" part. Following def, you write the name of the function. Ideally, you want to make your function name as descriptive as possible without being overly verbose. Commonly, Python programmers use underscores _ to separate words. Following the function name is a set of parenthesis. Optionally, arguments are defined within these parenthesis. We'll show that in a moment. After the parenthesis comes a colon. Up to and including this point is called the function signature. Less important, but still good to know. After the colon, the function body starts. The body consists of the code that will be executed whenever this function is invoked. Let's try it, then I'll explain.
print("=======", "We're gonna run print_hello()")
print_hello()
# You'll notice that the print statement in the function body ran. This is an example of a function invokation. Essentially, you just type in the function name along with parenthesis and whatnot. This is what we've been doing anytime we run the print function. Something to note in the function definition, all code within the body must be indented! Python uses indentation whitespace to know what code belongs to what other code. This way, the hello there print statement is inside the function, while saying that we're going to run the function is not inside the function. The only difference is the indentation. You'll see more of this later.

def print_fancy(a):
    print(a, "BUT FANCY!")
# Functions can also take in arguments, just like print. You can think of an argument like a variable that isn't set yet. It's set whenever the function is invoked. Let's show that.
print("=======", "We're gonna run print_fancy(\"Hi\")")
print_fancy("Hi")
# So what happened here? The argument "a" was set to the value of "Hi" when we invoked print_fancy. Then, inside the print_fancy function, whenever "a" was referenced, "Hi" was subsituted, just like any other variable. Do note that each invokation of a function is distinct and isolated. The "a" for this function call (invokation) disappears for future function calls. Each has its own value(s).

def print_add(a, b):
    print(a + b)
# We can also define multiple arguments for our functions. Similar to when we invoke print, you just separate them with commas.
print("=======", "We're going to run print_add(2, 3)")
print_add(2, 3)
# There shouldn't be any huge surprises here. The argument "a" gets set to 2. The argument "b" gets set to 3. We add these together and print the output.

# This is all fine and good for printing things, but what if we want functions to do things with data and then use that data? Arguments server as inputs, but how do we get outputs? There is a keyword "return" that will end a function and output whatever comes after (if anything).

def add(a, b):
    return a + b
print("=======", "We're going to run add(2, 3) and print it")
x = add(2, 3)
print(x)
# Note, we could also have written print(add(2, 3))
# This might be challenging to understand at first. Just like before, a becomes 2, b becomes 3, and they're added together to 5. After that, 5 is returned as the output of the add function. In this case, it kind of acts like a variable. Wherever add was invoked, the output value, 5, takes its place. The variable x is set to this output, and then we print x. Essentially, the output of a function is substituted wherever the invokation of that function happens. Lots of vocabulary, I know. Don't forget to check back in other areas for the definitions of things!
