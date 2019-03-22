import random
import sys


class Mob:
    def __init__(self, a, b, c, d):
        self.is_alive = a
        self.hp = b
        self.drop = c
        self.position = d


#########################
mobs = []
gains = {}

# {'ruby': 0, 'money': 0, ......., 'pistol': 0}

random_drops = ('Ruby', 'money', 'poop', 'candy', 'coin', 'paper',
                'key', 'password', 'girlfreind', 'pistol')

for i in range(100):
    mobs.append(Mob(1, 250,
                    random_drops[random.randint(0, len(random_drops)-1)],
                    (100 + i * 50, 100)))

for i in range(len(random_drops)):
    key = random_drops[i]
    value = 0
    gains[key] = value

while True:
    key = int(input('please input a number less than 100:'))

    if key == 999999:
        for i in gains:
            print(i, gains.get(i), end=' | ')
        sys.exit()

    if mobs[key].is_alive == 0:
        print('this mob is dead already!')
    else:
        mobs[key].is_alive = 0
        print('mob' + str(key) + ' is dead!')
        print('you have got a ' + mobs[key].drop)
        gains[mobs[key].drop] += 1


















