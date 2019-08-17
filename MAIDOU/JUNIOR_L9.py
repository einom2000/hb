word = 'abcdefghijklmnopqrstuvwxyz.!?, '
secret = input('please type in a secret:')
secret_lst = []
for i in range(len(secret)):
    secret_lst.append(secret[i])

encrypted = []
for l in secret_lst:
    index = word.find(l)
    index += 7   # key = 7
    encrpted_letter = word[index % 32]
    encrypted.append(encrpted_letter)

print('加密后的句子：' + ''.join(encrypted))
