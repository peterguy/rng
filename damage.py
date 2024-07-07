import random

# Simulate 1,000 dice rolls and calculate the average
num_rolls = 100_000
total_sum = 0
roll_count = 2
die_sides = 4
hit_bonus = 2

# Function to roll a single 4-sided die
def roll_die(sides = 4):
    return random.randint(1, sides)

# Function to roll two 4-sided dice and add 4 to the sum
def roll_and_add(count = 2, sides = 4, bonus = 4):
    sum = 0
    for _ in range(count):
        sum += roll_die(sides)
    sum += bonus
    return sum

for _ in range(num_rolls):
    total_sum += roll_and_add(roll_count, die_sides, hit_bonus)

average = total_sum / num_rolls

print(f"Average result after rolling {die_sides}-sided dice {roll_count} time(s), adding {hit_bonus}, and averaging over {num_rolls} rolls: {average:.2f}")
