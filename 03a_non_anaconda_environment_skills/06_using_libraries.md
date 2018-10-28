# Using Libraries

Surprise! This isn't a Python file. Don't worry, we'll be writing some code,
but most of the legwork is going to be in terminal. Let's get to it

## Concepts
### Packages and Modules
We covered modules a little bit before, but we'll review and extend our knowledge. A package is one or more modules in a manner that's easy to distribute. What makes it easy to distribute isn't important for your knowledge, unless you're making packages, which is unlikely. A module is either a file or folder of Python code that is meant to be used by other Python code. You likely wouldn't be writing any folder-drive modules, but file-based modules can simply be referenced by name. So if you have a file named `custom_logger.py`, you could simply do `import custom_logger`, and you would then have access to all the global variables and functions defined in that file, referencing them as `custom_logger.some_function_name()`. Magical.

### The Package Index
So how do you get packages of modules that other people have written? Say hello to the [Python Package Index, or PyPI](https://pypi.org/). Anyone can submit their package for listing on PyPI, and there are tools for easily downloading packages from this web repository. On the PyPI website, you can find some documentation on the package, the last update, a link to the source code for the package, and more. Usually, you don't need to do this, but it's a good reference if you're ever looking for more info.

### Keeping Your Environment Clean
Often, new developers will just install packages using the built-in tools without a care in the world. While quick and dirty, this can make life a nightmare when you get to the point of releasing your software or even when setting up on a new computer. To make sure that your dependencies, or packages that your code relies on, are portable, Python has the concept of a Virtual Environment. Virtual Environments are local copies of Python itself and Python libraries that are self-contained and self-documented. This way, if you install some dependency, you can track it easily, keep it separate from your other projects, and easily find it later if you ever need to setup the environment again. I'm not even going to teach you how to install packages outside of a Virtual Environment, so you'll be at least a little insulated from the potential pains of dependency hell.

## Doing the Things
### Getting the Tools
First, to download packages from PyPI, you need a tool called `pip`. Fortunately, Python 3 installs with `pip` already, so you don't need to worry about this. However, to setup our Virtual Environments quickly and easily, we can supplement `pip` with another tool: `pipenv`. `pipenv` effective just combines `pip` with Virtual Environment management. This abstracts managing the environment away from you and just makes your life easier. To install `pipenv`, open up a Terminal and run `sudo pip install pipenv`. Voila. After a few moments, `pip` will have installed the `pipenv` utility for you. You might get a warning about `pip` being out of date. If so, there's a command it will advise you to run - just go ahead and run it with `sudo` in front. Now that you're setup, run `pipenv --help` to get a brief rundown of what you can do with it.

### Setting Up Your Environment
First, check your version of Python with `python --version`. Next, run `pipenv --python 3.7` (assuming your Python version is 3.7.x). This will have `pipenv` setup a local environment based on Python 3.7, completely self contained from any other project. You should see a new file called `Pipfile`. This file tells `pip` and `pipenv` how your project is setup. Generally, a project is in some folder, and everything within that folder is related to the project. So when creating a new project, you should create a new folder for the project to reside in and do all your work within that folder. Congratulations on setting up your first virtual environment!

### Installing a Dependency Package
Now, we're going to install a new Python package called `requests`, which we'll use in the next file. Requests is a package that makes it easier to make HTTP requests over the internet for download webpages, downloading files, and more. Let's install requests to our new virtual environment: `pipenv install requests`. Boom. Done. You'll notice a new file: `Pipfile.lock`. This is just a safety file - it tracks the specific version and other metadata around dependencies that you've installed to this environment. So where is the requests module? Well, elsewhere. If memory serves, `pipenv` installs it to a hidden directory in your user's home folder. `pipenv` knows where the package is and will correctly reference it when you need it. The important parts that you should track are `Pipefile` and `Pipefile.lock`. These should be part of your project's Git repository, too. Make sure to `add` and `commit` them.

### Working in Your Virtual Environment
You have the requests package installed, but how do you actually use it? In your Python code, you can just `import requests`, and use it as documented, which will cover next lesson. However, there's one more step we need to do. If you just run `python` in your terminal now, it will run your system's Python, not the one setup in the Virtual Environment. There are two ways to run your Virtual Environment's Python.
1. Run `pipenv shell` to change this Terminal window's Python to the Virtual Environment's Python
2. Run `pipenv run python ...` where `...` is some Python file, anytime you want to run a file
There is no right or wrong way. It's just a matter of preference. Changing to the Virtual Environment shell is definitely more convenient, but you should keep in mind that your environment has been modified.

## Next...
Great job! Next up, we'll download files from the internet using the requests package we just downloaded. While this likely wouldn't be required often, it's a good skill to be familiar with just in case. Alternatively, if there's a case where you need to update your data from a file off the internet, this'll have you covered. See you in the next one!
