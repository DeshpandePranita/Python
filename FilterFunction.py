# Python filter() Function:
# Definition

# The filter() method constructs an iterator from elements of an iterable for which a function returns true.

# Syntax

# The syntax of filter() method is:

# filter(function, iterable)
# Parameters

# The filter() method takes two parameters:

# function – function that tests if elements of an iterable return true or false
# If None, the function defaults to Identity function – which returns false if any elements are false
# iterable – iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
 
# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
 
    if(alphabet in vowels):
        return True
    else:
        return False

filterdata = filter(filterVowels, alphabets) # filter(function, iterable)

print('The filtered vowels are:')
for vowel in filterdata:
    print(vowel)