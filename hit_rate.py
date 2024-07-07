import random

# Function to roll a single 20-sided die
def roll_die():
    return random.randint(1, 20)

# Simulate 1,000 dice rolls and count successes
num_rolls = 500
num_successes = 0
hit_base = 13

for _ in range(num_rolls):
    roll_result = roll_die()
    if roll_result >= hit_base:
        num_successes += 1

# Calculate the rate of success
success_rate = num_successes / num_rolls

# Output the rate of success
print(f"Out of {num_rolls} rolls, there were {num_successes} successes (roll >= {hit_base}).")
print(f"The rate of success was {success_rate:.2%}")
