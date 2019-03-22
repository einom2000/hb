# Crack the Caesar Cipher
# I got the dictionary, I don't have the key
# Try brutal force the cipher

alphabet = "abcdefghijklmnopqrstuvwxyz123456790 .,!?@"
length_alphabet = len(alphabet)

# get the cipher to hack
cipher = input("Please input the cypher you want to crack:").lower()
length_cipher = len(cipher)

# brutal force
for i in range(0, (length_alphabet - 1)):
    hack_key = i + 1
    hacked = ""
    # decoding
    for j in range(length_cipher):
        index = alphabet.find(cipher[j])
        index -= hack_key
        if index < 0:
            index += length_alphabet
        hacked += alphabet[index]
    print('If key is ' + str(hack_key))
    print('The cipher means: %s' % hacked)
# end of hack