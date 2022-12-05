#!/usr/bin/env python3

with open('input.txt') as f:
    text = f.read()

calories = [sum(int(num) for num in x.split()) for x in text.split("\n\n")]
print(max(calories))

calories.sort(reverse=True)
print(sum(calories[0:3]))
