#jwl4vg Jack Lesemann

import urllib.request


dictionary = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt').read().decode('utf-8').split('\n')
print('Type text; enter a blank line to end.')


user_string = input().split()


while user_string != '':
    check_list = []
    for words in user_string:
        check_list.append(words.strip('.?!,()\"\''))
    for word in check_list:
        if word.lower() not in dictionary and word not in dictionary:
            print('  MISSPELLED: ' + word)
    user_string = input()

