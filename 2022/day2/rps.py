#!/usr/bin/env python3

with open('input.txt') as f:
    input_text = f.read().split('\n')
    
# make list of play-tuples for easier access
plays = [(x[0], x[2]) for x in input_text]


abc = { 'A': 'rock', 'B': 'paper', 'C': 'scissors' }
to_win = { 'A': 'paper', 'B': 'scissors', 'C': 'rock'}
to_lose = { 'A': 'scissors', 'B': 'rock', 'C': 'paper'}

# part 1
xyz = { 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

# set up actual plays
battle_scores = { 
    'rock rock': 3,
    'rock paper': 6,
    'rock scissors': 0,
    'paper paper': 3,
    'paper rock': 0,
    'paper scissors': 6,
    'scissors scissors': 3,
    'scissors rock': 6,
    'scissors paper': 0
}

play_value = { 'rock': 1, 'paper': 2, 'scissors': 3}

total_score = 0
for their_play, my_play in plays:
    total_score += play_value[xyz[my_play]]
    current_play = abc[their_play] + ' ' + xyz[my_play]
    total_score += battle_scores[current_play]

print(total_score)

# part 2
strategy = { 'X': 'lose', 'Y': 'draw', 'Z': 'win' }

total_score = 0
for their_play, s in plays:
    if strategy[s] == 'lose':
        total_score += play_value[to_lose[their_play]]
    elif strategy[s] == 'draw':
        total_score += play_value[abc[their_play]] + 3
    else:
        total_score += play_value[to_win[their_play]] + 6
print(total_score)