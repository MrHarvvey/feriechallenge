import os
import re
from collections import Counter
from modulefinder import ModuleFinder

#how many tasks was done

def tasks_made(directory):
    # counting folders in directory each is treated as one task
    try:
        arr = os.listdir(directory)
    except :
        print("Directory does not exist")
    # check if directory includes hidden git folder if yes is subtracted
    if any(".git" or "README.md" in s for s in arr):
        count_task = len(arr) - 1
        if any(".git" and "README.md" in s for s in arr):
            count_task = len(arr) - 2
    else:
        count_task = len(arr)
    return count_task


# getting all files form directory with extension .py and return list of this files
def get_py_file(directory):
    list_of_files = []
    for root, dirs, files in os.walk("/home/oskar2333/PycharmProjects/#feriechallange"):
        for file in files:
            if file.endswith(".py"):
                list_of_files.append(os.path.join(root, file))
    return list_of_files



#count how many lines i wrote in directories excluding empty one

def count_lines(list_files):
    lines = 0
    for file in list_files:
        with open(file) as infp:
            for line in infp:
                if line.strip():
                     lines += 1
    return lines


#creating one file from many

def one_file(list_files):
    with open("all.txt", "w") as outfile:
        for filename in list_files:
            with open(filename) as infile:
                contents = infile.read()
                new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', contents)
                outfile.write(new_str)

#counting  unique words in file

def unique_words(file):
    return len(set(w.lower() for w in open(file).read().split()))


def most_common_word(value):
    words = open("all.txt", "r").read().split()  # read the words into a list.
    return Counter(words).most_common(value)

def print_common(value):
    list_common = most_common_word(value)
    for idx, word in enumerate(list_common):
        print(f'Position {idx + 1} was: {word[0]} occoured {word[1]} times')


print(f'Congratulations you made {tasks_made("/home/oskar2333/PycharmProjects/#feriechallange")} from 10 tasks and you wrote {count_lines(get_py_file("/home/oskar2333/PycharmProjects/#feriechallange"))} lines of code !!')
one_file(get_py_file("/home/oskar2333/PycharmProjects/#feriechallange"))
print(f'You wrote {unique_words("all.txt")} unique words')
print(f'Most common word: {most_common_word(1)[0][0]} used {most_common_word(1)[0][1]} times')
print_common(5)


def find_modules2():
    dataLog = []
    with open('all.txt', 'rt') as f:
        data = f.readlines()
    for line in data:
        if line.__contains__('import '):
            dataLog.append(line)
    print(dataLog)

find_modules2()

