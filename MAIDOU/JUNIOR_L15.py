import time
import random
import sys

def generate():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    sample = ''
    for _ in range(0, random.randint(1, 2)):
        for i in range(0, random.randint(5, 10)):
            word = ''
            for _ in range(0, random.randint(2, 7)):
                word += alpha[random.randint(0, 25)]
            if i == 0:
                word = word.title()
            sample += word + ' '
        sample = sample[:-2]
        sample += '. '
    return sample


typing_sample = generate()
print('PLEASE TYPE THE FOLLOWING SENTENCES:', file=sys.stderr)
time.sleep(1)
t1 = time.time()
line = input(typing_sample)
t2 = time.time()

seconds = int(t2 - t1)
minutes = seconds // 60

error = 0
for i in range(0, len(line)):
    if line[i] != typing_sample[i]:
        error += 1
corrective_percent = (len(typing_sample) - error) / len(typing_sample) * 100

print('You use %d minutes and %d seconds at %d percent accuracy!'
      %(minutes, seconds, corrective_percent))
