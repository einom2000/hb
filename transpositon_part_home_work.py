# Transposition cipher


def caesar_cipher():
    word = input('Please input a word to cipher: ').lower()
    ciphered = ""
    for i in range(len(word)):
        ciphered += tuple_dic[0][(tuple_dic[0].find(word[i])
                                  + int(tuple_dic[1][i % len(tuple_dic[1])]))
                                 % len(tuple_dic[1])]
    return ciphered


def main():
    global tuple_dic
    tuple_dic = ("abcdefghijklmnopqrstuvwxyz123456790 .,!?@",
                 "1216172633871263879162378162781873687126387912687")
    print(caesar_cipher())


if __name__ == '__main__':
    tuple_dic = ()
    main()
