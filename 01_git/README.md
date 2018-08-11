# Git

Git is a source control management (SCM) system. Its predecessors include Subversion (SVN) and Concurrent Versions System (CVS), but that's just for trivia. Git allows you to record changes in code over time. It tracks what changes were made, when, and by whom. You can add additional information to describe the changes that were made, and tools exist to help you compare different versions of your code.

Git is distributed in nature. This means that you can have a copy of the code, and another copy of the code can live elsewhere. This leads to some interesting but sometimes useful mechanisms between copies. The major thing to keep in mind is this: most operations happen on your local copy of the code; if you want to change other copies, the action must be done explicitly. Fortunately, most of the time you'll just be taking all of the changes you've made and syncing them with remote copies. More details on that in a bit.

There was a super slick interactive Git tutorial that Github had, but it seems to be gone. For future sections, they'll be more of me pointing to tutorials than teaching directly.

## Setting Up
### Updating Git
On Mac, Git is already installed, though you may want to update it. Rather than repeat things, [check out this Medium post for upgrading Git](https://medium.com/@katopz/how-to-upgrade-git-ff00ea12be18).

### Creating a Project
For cleanliness, projects usually live in one main folder. Git knows this and operates accordingly. Setup a folder somewhere on your machine for what we'll be doing here. In Terminal, navigate into that folder, and run this:
```bash
git init
```
This will create a folder `.git`. This is where all of the information that Git needs for this project is stored. Old versions, configurations, and more are stored in this folder. Can't see it? Add a `-a` to your `ls`/`ll` command. The only file you really need to know about is `.git/config`. Every once in awhile, you might mess things up and need to hand-edit `config`. Just something to keep in the back of your end.

### Ignoring Unnecessary Shit
Git recognizes a few key filenames. One of these is `.gitignore`. This file is just a listing of files that Git should ignore. Have a configuration file with passwords in it? Toss the name of it into `.gitignore`. Have compiled objects or data files that other people shouldn't need or want to download? Toss their paths in `.gitignore`. Each line within `.gitignore` should have a path that Git will just bypass when it sees it. You can look at the `.gitignore` file in this repository as an example.

### Not Losing Necessary Shit
Chances are, you don't want to lose your code. As mentioned before, Git is distributed in nature. We can backup your code to somewhere its unlikely to be lost. Where? Most developers use [Github](https://github.com) (just like you are now). If you don't already have one, create an account and create a new repository. The defaults are okay; just enter the name for now. Bear in mind, things you put here are public - the whole world can see them. Don't put anything on Git that you don't want people to see. Now, let's get your empty project on Github.

Fortunately, Github actually provides the instructions on how to do this if you create a completely empty repository. However, we're going to walkthrough things step-by-step here, so you know what's going on.

In your directory in Terminal, run `git status`. This will tell you the current state of the Git repository (project). Are there new files? Are there changes to files? Are there files that are in the folder but that Git isn't tracking? `status` will tell you the answers to all of these questions.

Here's a listing of the different states of files as shown in `status`. You may want to just keep this spot in mind to reference later:
* `Untracked files` are files that are in the directory, but Git doesn't know what to do with them.
* `Changes not staged for commit` means that Git recognizes files it's tracking have changed, but it's not been told to do anything about it.
* `Changes to be committed` are files that have changed that Git has been told to keep track of the changes.

Anytime you add a new file to a Git repository (project), it will be untracked. If you want Git to keep track of the changes, you need to tell Git to add it to the project. This is pretty simple. Just run `git add <filename>` where `<filename>` is the name of the file you want to add. You can have several files in one command, and Git understands wildcards (\*). If you know you want to add every file (that's not ignored) to be tracked, you can just use `git add -A`. Go ahead and do that now.

Now, if you run `git status`, you'll see that your `.gitignore` file is being tracked. We've told Git that we plan on tracking it by using `add`, but we haven't actually recorded anything yet. To do that, we need to create a **commit**. A commit is a snapshot of the project in time. It contains all of the changes that have been made since the previous commit (or the current state of the project if it's the first commit), the information of the person who made the change, when the change was made, and a brief message describing the commit. We're going to tell Git to create a commit to record our changes. This is also used as a verb: committing our changes.

Run `git commit`. Now, if this is your first time running `commit` on this laptop, Git will prompt you to give it some information about who you are. Git uses this to provide author information for the creator of the commit. Bear in mind, if you're putting things on Github (which we are), this information will be public. After filling out whatever information Git wants, run `git commit` again. You'll be brought into a Vi editor. This is where you'll enter the commit message, which should be a short blurp describing the change you made. The first line is usually a title for the commit, while any following lines describe things more in-depth. Hit `i` to enter Insert mode to make your changes. When finished, hit `esc` to enter command mode. To write your message to the commit and exit the Vi editor, enter `:wq`. Congratulations, you've made your first commit!

Now, back on your Github repository, it should have some instructions up to this point. Next, you'll want to run the `git remote add` command that they list. Run it as they've written it, since I don't know in advance what your repository's URL will be. A `remote` in Git is simple a copy of your repository on another computer. Remember earlier how I mentioned that Git was distributed? This is it in action. By committing your code, you made a checkpoint in time of things, but it still only lives on your computer. Running the `remote add` command tells your local copy of the repository that another copy exists somewhere out there.

Now that you've told your local repository about the remote, you can `push` your changes to the remote version. This **overwrites** any changes the remote copy has. The nice part is that Github will warn you if you try to change any history its already recorded. On your Github repository page, it should say something like `git push -u origin master`. This tells your local repository that the remote called `origin` and the branch called `master` should be considered "upstream" of your current branch. I know the branch part may not make sense now, so just know that it establishes a relationship between your current set of code and the code on the remote. In the future, you can just run `git push` without any of the stuff after it. After you've run this, your project will be on Github! If you refresh the page, you'll see your `.gitignore` file up there.

## The Workflow
After this section, you may want to pause. We'll cover the common workflow you'll use in a single-person project that's not too complex. It basically follows this:
1. Make changes to your code
2. Decide on a good stopping point - something is working or you're about to try an experiment
3. Use `git add` to track the changes you've made
4. Use `git commit` to record the changes you've made and add a message describing the changes so your future self can love your past self
5. Use `git push` to take all of your local commits and get them up on Github in case your laptop 'splodes.
6. Relax because your code is safe.

## Moving Forward
Now that you have some of the basics, check out this site for the more advanced stuff: https://learngitbranching.js.org/
