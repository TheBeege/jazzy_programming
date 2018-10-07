#!/usr/bin/env python3

# Now for the good stuff. So let's say you got some sweet, juicy data
# off of Kaggle or something. That data is gonna be in a file or a collection
# of files. We're gonna go over how to get a hold of that data to do all
# the things with it

from pathlib import Path
# Surprise! What's this? It's a module. Modules are magical and terrifying.
# Modules are libraries of code to do stuff for you, since we're not here
# to reinvent the wheel. Path is a new thing in Python 3 (I had to look it up)
# that allows you to get the filesystem path of a file. Since I don't know
# exactly how you're going to be running this program, I'm going to use
# this to make sure I'm in the correct directory (the directory of this script)

script_dir = Path(__file__).resolve().parent
print('script_dir:', script_dir)
# This gets you the directory of the this script. The __file__ variable is a
# built-in variable that has the location of the current file. Using pathlib,
# we can create a path out of this, get the absolute path on the filesystem,
# then ask for the parent directory. There's a little bit of object-oriented
# stuff going on here, so please pardon a bit of hand-waving

sample_file_path = script_dir.joinpath('supporting_files')\
    .joinpath('sample_file.txt')
print('sample_file_path:', sample_file_path)
# At this point, we have a Path that points to our sample file. Pardon the
# backslash followed by a newline and tab. That's just a way to keep the line
# from getting too long. Now, let's open up our file

with sample_file_path.open() as file:
    # At this point, we use our Path to open up the file and store it in a
    # variable called file. This "with ... as ...:" is specific to opening
    # streaming data. Streaming data could be something like a file or a network
    # connection to some other data. The "with" indicates that we're opening a
    # stream, and that the indented block beneath it should be executed while
    # the stream (file) is open. When the indentation stops, the stream (file)
    # will be closed an inaccessible. This is useful because the operating
    # system may put a lock on the file while it's open, preventing other
    # programs from accessing it. Additionally, having files open costs some
    # amount of resources, so you want to make sure to reclaim the resources
    # spent opening the file as quickly as possible. The "with" construct
    # just makes it easier. It does all the closing and checking for you

    print('contents of sample_file.txt:', file.read())
    # Tada! You've read the contents of the file. It's... pretty simple.
    # But what if you want to read the file? We can't actually do that here.
    # The way we've opened this file, we can only read from it. Honestly,
    # you probably won't need to edit files terrible much, so we're not gonna
    # worry about that for now. Let's try working with a file line by line

sample_file_path = sample_file_path.parent.joinpath('multiline.txt')
with sample_file_path.open() as file:
    # Okay, we've gone back to the supporting file directory and grabbed the
    # file multiline.txt. We've opened it up, and now we can work with it

    line_list = [] # Ignore this for now :)

    for line in file:
        print('line:', line)
        # When you iterate over a file like it was a collection, Python does
        # some smart stuff for you. It treats each line like an item in
        # a collection. You'll notice the output may look a little weird.
        # Python is adding a newline character at the end, and this is
        # shown when you print it. Regardless, this is a good way to get
        # data out of a file when you want to work line by line. If you're
        # going to be doing some heavy lifting, I recommend you read all the
        # data into a list, let the file close, then play with the list

        line_list.append(line.strip())
print('line_list:', line_list)
# Remember that line_list variable we setup? We wanted to create the
# list before we started looping. If we created it inside the loop, it
# would be recreated every time the loop ran, giving us a list with only
# the last line. Instead, we create an empty list before looping, then
# we append the line each time we loop through. The strip() function
# strips any whitespace off the end of a string, including whitespace.
# Now, we have a nice, clean list of lines from the file, and the file is closed

# So... that's all good, but we can do better. Chances are, the data you're
# grabbing is in some sort of format, most like a CSV or comma separated values.
# Luckily, Python has a built-in library specifically for that. Let's try it

sample_file_path = sample_file_path.parent.joinpath('people.csv')
# Get the path to our file. This is my first time using pathlib... It's WAY
# easier than how we used to do it. Back in my day, we had to count out
# bits up a one mile hill covered in snow and convert the binary to text
# #oldGeezerThings

import csv
with sample_file_path.open() as file:
    csv_reader = csv.reader(file)
    # Oh baby. Now we're cooking with fire. First, we need to import the csv
    # library to get out our bag of fairy dust. Next, we just say fuck it,
    # and dump the file into our fairy dust bag's reader() function.
    # The csv library does different things for reading and writing, but
    # you're likely going to be more concerned with reading. After that, we
    # can iterate through it just like we would a file. This time, however,
    # each iteration will give us a list

    for row in csv_reader:
        print('csv row:', row)
    # Nice! Each row is now a list we can do stuff with. But hey, notice how
    # the first list is actually the field names for the remaining rows. This
    # won't always be the case, but we can actually do something with that

    file.seek(0)
    # This puts us back at the beginning of the file

    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print('row name:', row['name'])
        print('row email:', row['email'])
        print('row profession:', row['profession'])
        print('---------------------')
# Now we gettin' fancy! When using a DictReader, it reads in the first row of
# the CSV file and interprets them as field names. From there, if you iterate
# through the file, each row will be a dictionary, where the keys are the
# field names, and the values are the corresponding value for that row

# Great job getting this far! This should be all the absolute basics you need
# for writing simple Python programs. 
