import os


print(os.getcwd())
# This code snippet returns the current working directory.

os.mkdir("new_dir")
# The os.mkdir("new_dir") function creates a new directory called new_dir
# in the current working directory.


os.chdir("new_dir")
os.getcwd()
# This code snippet changes the current working directory to new_dir.
# The second line prints the current working directory.


os.mkdir("newer_dir")
os.rmdir("newer_dir")
# This code snippet creates a new directory called newer_dir.
# The second line deletes the newer_dir directory.

os.listdir("website")
# This code snippet returns a list of all the files and
# sub-directories in the website directory.

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
