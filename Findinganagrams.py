# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    
    word1 = word.lower()
    anagram1 = anagram.lower()
    
    sortedword1 = sorted(word1)
    sortedanagram1 = sorted(anagram1)

    
    if(sortedword1 == sortedanagram1):
        return True
    else:
        return False
    
gram = find_anagrams("CONserVAtion", "conversation")
print(gram)





    
