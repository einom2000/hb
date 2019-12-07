score = {"luca"  :149,
         "david" :130,
         "lucy"  :100,
         "kidd"  :128,
         "max"   :123,
         "daisy" :105,
         "mike"  :132,
         "jack"  :80,}

for mingzi in score.keys():
    print(mingzi)

print(score.items())

name = input("please add a student name")
sc=int(input("please input this score:"))
score[name] = sc
print(score)


level = input("please input a level score")
level = int(level)

for mingzi,chenji in score.items():
    if (chenji)>= level:
        print(mingzi + ":" + str(chenji))


