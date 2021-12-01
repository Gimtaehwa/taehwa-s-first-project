import random

voca_dictionary = {}
with open ("vocabulary.txt", "r") as f:
    for line in f:
        data = line.strip().split()
        eng, kor = data[0], data[1]
        voca_dictionary[eng] = kor


        
while True:
    num = random.randint(1, len(voca_dictionary))

    a = input("{}: ".num in voca_dictionary.keys())
    




