#!/usr/bin/env python3

with open('input.txt') as f:
    text = f.read().split()

# setup input as tuples for easier access
assignment_pairs = [(pair[0].split('-'), pair[1].split('-')) for pair in (line.split(',') for line in text)]

# helper 
def elf_sections(pair):
    first_elf, second_elf = pair
    first_elf_start, first_elf_end = first_elf
    second_elf_start, second_elf_end = second_elf
    return (int(first_elf_start), int(first_elf_end), int(second_elf_start), int(second_elf_end))
    
# part 1
def completely_overlapping(pair):
    e1_start, e1_end, e2_start, e2_end = elf_sections(pair)
    
    return int(e1_start) <= int(e2_start) and\
           int(e1_end) >= int(e2_end) or\
           int(e2_start) <= int(e1_start) and\
           int(e2_end) >= int(e1_end)

complete_overlaps = [pair for pair in assignment_pairs if completely_overlapping(pair)]
print(len(complete_overlaps))

# part 2
def some_overlap(pair):
    e1s1, e1s2, e2s1, e2s2 = elf_sections(pair)
    
    overlaps = range(max(e1s1, e2s1), min(e1s2, e2s2))
    return overlaps.start <= overlaps.stop
    
some_overlaps = [pair for pair in assignment_pairs if some_overlap(pair)]
print(len(some_overlaps))