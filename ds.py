# manipulating strings
# str = "Hello"
# str1 = str + " Name"
# print(str1)

# fruit = 'banana'
# print('n' in fruit) # use in as a logical operator

# string comparision
# word = input("Enter a word: ")
# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('All right, bananas

# string library has many functions
# print('Hi there'.lower())
#
# stuff = '  Hello world'
# type(stuff) # returns data type
# dir(stuff) # returns all the functions/methods within string class
#
# part = stuff.replace('world', 'love') # replaces first param with second one
# print(part.strip()) # removes whitespace at beginning and end, lstrip/rstrip
#
# # parsing/extracting
# data = 'Anytime hartfor.poland@unt.ac.za Sat Jun 5 09:13:10 2003'
# atpos = data.find('@') # 21
# sppos = data.find(' ', atpos) # 31
#
# host = data[atpos+1 : sppos] # 22 to 30
# print(host) # prints unt.ac.za

'''
string mutation: given user input of string, num, and letter,
string is replaced by letter at position of the num
'''
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

'''
string traversal: given user input of string and a substring, we must print
the number of times that the substring occurs in that string
'''
def count_substring(string, sub_string):
    count = 0
    found_index = string.find(sub_string)
    while found_index != -1:
        count +=1
        found_index = string.find(sub_string, found_index + 1)

    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

'''
if there's any char in the string that matches the method conditions, return
ture else false
'''
s = input()
# any(boolean for x in list/string) checks if boolean applies to any index
print(any(c.isalnum() for c in s)) #a-z, A-Z, 0-9
print(any(c.isalpha() for c in s)) #a-z, A-Z
print(any(c.isdigit() for c in s)) #0-9
print(any(c.islower() for c in s)) #a-z
print(any(c.isupper() for c in s)) #A-Z
