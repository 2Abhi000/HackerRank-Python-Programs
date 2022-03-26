'''
python: String TransformationThere is a sentence that consists of
space-separated strings of upper and lower case English letters.
Transform each string according to the given algorithm and return
the new sentence. Each string should be modified as follows:The
first character of the string remains unchangedFor each subsequent
character, say x, consider a letter preceding it, say y:
If y precedes x in the English alphabet, transform x to uppercase
If x precedes y in the English alphabet, transform x to lowercase
If x and y are equal, the letter remains unchanged
Examplesentence = "coOL dog" The first letters of both words remain unchanged.
Then, for the word "coOL" the first "o" is made uppercase because the
letter preceding it, "c", comes earlier in the alphabet. Next,
the case of the second "O" is unchanged because the letter preceding is
also "o", and finally the "L" is made lowercase because the letter
preceding it, "O", comes later in the alphabet. The second word,
"dOg", is transformed according to the same rules. Return the resulting
sentence 'cOOl dOg'.'''

import math
import os
import random
import re
import sys

def transformSentence(sentence):
    l=sentence.split()
    
    li=[]
    st=""
    for i in l:
        st+=i[0]
        for j in range(0,len(i)-1):
            if(i[j].lower()<i[j+1].lower()):
                st+=(i[j+1].upper())
            elif(i[j].lower()>i[j+1].lower()):
                st+=(i[j+1].lower())
            else:
                st+=i[j+1]
        li.append(st)
        st=""
    result=""
    
    for i in li:
        result=result+" "+i
    return (result.strip())
sentence=input()
x=transformSentence(sentence)
print(x)
