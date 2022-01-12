import random
words_list=[]
random_num = random.randint(0, (len(words_list) - 1))
current_word = list(words_list[random_num].upper())
print(current_word)
print('The word has', str(len(current_word)), 'characters')

current_letter = input('Pick a letter: ').upper() #User input
picked_letters = []
correct_ones = []
for i in range(len(current_word)):
    correct_ones.append('_ ')
print(correct_ones)