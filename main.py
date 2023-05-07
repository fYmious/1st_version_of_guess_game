import random
f = open('sowpods.txt', 'r')
words = [i[:-1] for i in f]
start_word = (random.choice(words)).lower()
# print(start_word)
final_word = list('*' * len(start_word))
while True:
    char = str(input('введите букву: '))
    while len(char) != 1:
        char = str(input('введите букву: '))
        if str(len(char)) == 1:
            char = (char).lower
            break
    if char in start_word:
        if start_word.count(char) == 1:
            ind = start_word.index(char)
            final_word[ind] = char
            print('буква в слове!!!')
            print(final_word)
            print('________________')
            final_word = final_word
        elif start_word.count(char) > 1:
            for i in range(len(start_word)):
                if start_word[i] == char:
                    final_word[i] = char
            print('буква в слове')
            print(final_word)
            print('________________')
            final_word = final_word
    else:
        print('буква не в слове (((')
        print(final_word)
        print('________________')
        final_word = final_word
    if not('*' in final_word):
        break 
final_word = ''.join(final_word)
print('________________')
print(f'поздравляем, вы угадали слово {final_word}')