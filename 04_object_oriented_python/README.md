# Object-Oriented Python

Python supports an object-oriented model of programming. Object-oriented programming, or OOP, is a way to make code more modular and help developers think about things more easily. The idea is that programming often models the real world, and the real world is full of objects. As such, some programming languages have some concept of objects.

If you're in a super hurry, you may want to skip this whole section. This will help you debug problems more effectively, but I'm not sure if OOP is a necessary concept in data science.

## What is an Object?
An object really has two key things: it has properties, and it can do things. Properties translates to variables, and doing things translates to methods. So really, an object is just a way of group variables and methods together. However, these variables and methods are separate from the rest of the code. This is called encapsulation. An object encapsulates its variables and methods, keeping them separate from everything else.

An object can be stored inside a variable. Then, when access that variable, you can access the variables and methods stored inside the object. Objects can even store other objects within their variables. This makes sense when comparing to the real world. There might be a `Person` object. It might have a variables called `arms` that contains a tuple of `Arm` objects. An `Arm` object may have another variable called `elbow`. Stored inside this could be an `Elbow` object, and that `Elbow` could have a method called `bend()`. Since each `Elbow` is distinct from any other object, `bend()`ing one `Elbow` will have no bearing on the other. Likewise, each `Arm` contains its own unique `Elbow`, again distinct from anything else. This sort of structure allows us to accurately describe the world in ways that make some amount of sense.

Now that the concept is out there, let's try creating some objects ourselves. See you in [01_classes_and_objects.ipynb](./01_classes_and_objects.ipynb)!
