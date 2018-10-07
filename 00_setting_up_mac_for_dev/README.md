# Setting Up
Before we dive into things, there are some general tools that you'll want to install to make life easier for you in the future. Let's get it done.

## XCode Utilities
Many things depend on common packages like the GCC compiler, which is used for compiling C programs. If that sounds like Greek to you, don't worry about it. Just know that you need it. These common packages are easily downloaded and installed using XCode. Rather than repeat things, you can find a quick run-through here: http://railsapps.github.io/xcode-command-line-tools.html

## Homebrew
Homebrew is a package manager for dev tools on Mac. [The Homebrew webpage has a single-line install command.](https://brew.sh/) Run that, and you should be all set!

## Anaconda
Download and install [Anaconda](https://www.anaconda.com/download/). Anaconda is a Python development environment specifically designed for data science, rather than general software development. Anaconda includes Jupyter Notebook and a wide range of packages commonly used within data science.

### Why is Anaconda different from general development?
In general software development, you want individual projects to be separate. This simplifies later deployment, since libraries your application depends on will be independent of each other. This separation of code makes packaging and deployment easier, especially when you could be deploying to different types of environments. Data science doesn't need this separation. Most often, you'll likely use the same libraries from project to project, making the separation of these dependencies a moot point. Additionally, the product of data science is often reports, not software bundles. This means there's no deployment, meaning the need for separation is even less. That said, there is still value to separate Jupyter notebooks for separate projects and tasks, but Anaconda provides for that. With this in mind, be aware that Anaconda is _huge_. It includes over 1,000 dependency packages, which adds up. Installation will take some time.
