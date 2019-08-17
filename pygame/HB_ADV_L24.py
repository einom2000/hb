class Mob(object):
    hungry = 'yes'
    alive = True
    def __init__(self, a, b):
        self.hp = a
        self.mp = b

    def hit(self, h):
        self.hp -= h
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def hurt(self):
        self.hp = 1

tommy = Mob(100, 999)
jerry = Mob(800, 70)

tommy.hp -= 10
print(tommy.hp)
print(tommy.mp)
tommy.hungry = 'No'
print(tommy.hungry)

jerry.hungry = 'No'
print('Jerry health is: ' + str(jerry.hp))
print('Jerry magic power is: ' + str(jerry.mp))
print('Is Jerry hungry ? ' + jerry.hungry)

tommy.hit(199)
print('Is Tommy alive? ' + str(tommy.alive))
print('Tommy was attacked, now tommy hp is: ' + str(tommy.hp))

jerry.hit(367.833)
jerry.hurt()
print(jerry.alive)
print('Jerry was attacked too, now Jerry hp is: ' + str(jerry.hp))
