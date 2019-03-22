# f = open('123.txt', 'w')
# f.write('Today is my birthday. \nI love to have a party. \nEnjoy my party!')
# f.close()

"""my transposition cipher program ver 0.8
    my transposition cipher program ver 0.8
    my transposition cipher program ver 0.8"""
# my transposition cipher program ver 0.8


def cipher(words, key):
    ciphered = [''] * key
    for column in range(key):
        current_index = column
        while current_index < len(words):
            ciphered[column] += words[current_index]
            current_index += key
    return ''.join(ciphered) + '|'


def main():
    keyin = input('please type in the words and key to cipher: ')
    tmp_list = keyin.split(',')
    key = int(tmp_list[-1])
    words = ','.join(tmp_list[:-1])
    print(cipher(words, key))
    pass

f = open('123.txt', 'r')
lines_ciphered =[]
for line in f.readlines():
    print(line, end='')
    lines_ciphered.append(cipher(line, 4))
f.close()

k = open('4567.txt', 'w')
for line in lines_ciphered:
    k.write(line)
k.close()








