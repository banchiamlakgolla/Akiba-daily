print("=================================")
print("      Palindrome checker")
print("=================================")

word = input("Enter the word you want to check: ")
word = word.lower()

reversed_word = word[::-1]

if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
    
# using for loop
# reversed_word = ""
# for letter in word:
#     reversed_word = letter + reversed_word

# if word == reversed_word:
#     print("The word is a palindrome.")
# else:
#     print("The word is not a palindrome.")