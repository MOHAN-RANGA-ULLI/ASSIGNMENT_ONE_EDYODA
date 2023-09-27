word = input('enter the word:')
l=len(word)

for i in range(1, l+1):
    print(word[-i] , end='')

## second method

# word = input('enter the word:')

# reverse_of_word = " "

# for i in word:
#     reverse_of_word = i + reverse_of_word
# print('reverse of the given word is:' , reverse_of_word)