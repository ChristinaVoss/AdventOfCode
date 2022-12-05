#!/usr/bin/env python3

with open('input.txt') as f:
    backpacks = f.read().split()
    
def set_priority(letter):
    if letter.isupper():
        priority =  ord(letter) - 38
    else:
        priority =  ord(letter) - 96
    return priority

# part 1
items = [(set(item[:int(len(item)/2)]) & set(item[int(len(item)/2):])).pop() for item in backpacks]
total = sum([set_priority(letter) for letter in items])

print(total)

# part 2
badges = []
for i in range(0, len(backpacks), 3):
    backpack_1 = set(backpacks[i])
    backpack_2 = set(backpacks[i+1])
    backpack_3 = set(backpacks[i+2])
    badges.append(set_priority((backpack_1 & backpack_2 & backpack_3).pop()))

print(sum(badges))
    
