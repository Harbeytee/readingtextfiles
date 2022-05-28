# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from cgi import print_directory
import string
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        contents = f.read()
        
    return contents


def count_words():
    text = read_file_content("./story.txt")

    split_text = text.split()
    dic ={}
    for word in split_text:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


new = count_words() 
print(new)

