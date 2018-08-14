# Procedural Python

Here, we're gonna cover the basics of Python. I've separated Python into procedural and object-oriented sections. Procedural is enough to get you started, but doing things in an object-oriented manner can help you organize code or at least understand others' systems and how they might work. We'll start with installing the latest version of Python.

## Installing Python with Homebrew
It's easy. Open terminal and run this:
```shell
brew install python
```

Run this to make sure you get a Python 3.x.x version:
```shell
python --version
```

You should be all set!

## Running Python Scripts
First, toss a simple "Hello, world!" program into a `.py` file:
```python
print("Hello, world!")
```
Save it to `hello.py`. We'll use this file for this section.

There's effectively two ways to run scripts:
1. Run using the interpreter
2. Run from the shell by listing the interpreter in the file

### Running Python scripts using the interpreter
In terminal, you can simply navigate to wherever the script is located and run `python hello.py`. This explicitly calls the Python interpreter. The interpreter by default takes in one argument: the script to run. It's that easy. However, we're lazy, and we can do better.

### Running Python from the shell with shebang
Shebang is short for hash-bang. Hash is `#`. Bang is `!`. If the very first line of a file starts with a shebang `#!`, then terminal will try to give the file as an argument to whatever program is listed after the shebang. Commonly, we use `#!/usr/bin/env python` or `#!/usr/bin/env python3` if you're picky. The `env` executable looks throughout your environment to find an executable whose name matches the argument. If `python` is installed in `/bin`, `/usr/bin/env python` will return `/bin/python`. We do this because we may not necessarily know where Python is installed, or we don't care, or both! Whatever is output by `env` will take the place of the shebang. Whatever is at the shebang, terminal will use to run this file. Go ahead and add this as the **very first** line in your `hello.py` file:
```python
#!/usr/bin/env python3
```
Then tell the shell we should be allowed to execute it, and run it from the shell directly:
```shell
chmod u+x hello.py
./hello.py
```
Now, we can just use `./hello.py` to run our file. Less typing. More win.

The `chmod u+x hello.py` command modify the permissions for the file. Let's break it down:
* `chmod` is the command to alter permissions
* `u` denotes the user that owns the file. Other possibilities are `g` for owning group, `o` for others (anyone), or `a` for all.
* `+` means we're adding permissions. You could also use `-` to remove permissions.
* `x` is the execute permission. Other options are `r` for read and `w` for write.
By default, files don't have execute permission. It's kind of a safety mechanism to make unwanted files more difficult to execute, but it does require us to add the execute permission anytime we create a new script. It's something to keep in mind. Try removing the execute permission and running it again. This way, you'll know what the permissions error looks like for the inevitable time when you forget to add the execute permission.

## Writing Actual Python
Enough exposition. Let's dive in. In this folder, there are python files numbered in order. Each one has code and comments. We'll cover each topic, and you should be good to go!
