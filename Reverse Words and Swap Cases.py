'''
python: Reverse Words and Swap CasesImplement a function that takes a
string consisting of words separated by single spaces and returns
a string containing all those words but in the reverse order and
such that all cases of letters in the original string are swapped,
i.e. lowercase letters become uppercase and uppercase letters become lowercase.
Examplesentence = "rUns dOg" Reverse the word order and swap the case of
all letters, then return the string "DoG RuNS".
'''
def reverse_words_order_and_swap_cases(sentence):
    ar=sentence.split()
    k=''
    for i in ar[::-1]:
        k+=i
        k+=' '
    l=k.swapcase()
    return(l)
sentence=input()
x=reverse_words_order_and_swap_cases(sentence)
print(x)
