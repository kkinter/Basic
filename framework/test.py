import random

menu = ["사과", "딸기", "포도"]
word_li = ["바나나", "짜장면", "사과", "포도", "딸기"]
print(random.randint(0, 10))
word = 99
li = [x for x in range(word)]
random.shuffle(li)
print(li)
