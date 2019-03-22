# Transposition Cipher Decryption


import math

message = 'Cenoonommstmme oo snnio. s s c'
key = 8

numOfColumns = int(math.ceil(len(message) / float(key)))
# math.ceil:  returns the smallest integer greater than or equal to a given number.
numOfRows = key
numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

plaintext = [''] * numOfColumns

column = 0
row = 0

for symbol in message:
    plaintext[column] += symbol
    column += 1

    if (column == numOfColumns) or (column == numOfColumns - 1 and
        row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
print(''.join(plaintext))

