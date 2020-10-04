import sys
import os
import datetime

def NewPost(title = "New Title", tags = []):
    currDate = datetime.datetime.now()
    DateStr = currDate.strftime("%Y-%m-%d")
    TimeStr = currDate.strftime("%H:%M:%S %z")

    path = "./_posts/"
    filename = path + DateStr + "-" + title + ".md"

    file = open(filename, "x")
    file.write("---\n")
    file.write("title: " + title + "\n")
    file.write("date: " + DateStr + " " + TimeStr + "\n")
    file.write("tags: [")
    for tag in tags:
        file.write(tag + ",")
    file.write("]\n")
    file.write("---\n")

    file.close()

if __name__ == "__main__":
    NewPost(sys.argv[1])