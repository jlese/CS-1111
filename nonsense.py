word = input("What is your favorite word? ")

string_length = len(word) + 1
final_word = word.ljust(string_length)

print(final_word * 12) #also could list word out 12 times with commas

print('"' + word + '"' + " doesn't even sound like a word anymore")
