import random

def flip_coin():
    """Simulate flipping a coin."""
    return random.choice(['heads', 'tails'])

def count_consecutive_flips(num_flips):
    """Count the highest amount of consecutive heads and tails."""
    max_heads = 0
    max_tails = 0
    current_heads = 0
    current_tails = 0

    for _ in range(num_flips):
        result = flip_coin()
        if result == 'heads':
            current_heads += 1
            current_tails = 0
            if current_heads > max_heads:
                max_heads = current_heads
        else:
            current_tails += 1
            current_heads = 0
            if current_tails > max_tails:
                max_tails = current_tails

    return max_heads, max_tails

num_flips = 60_000_000  # Number of coin flips
max_heads, max_tails = count_consecutive_flips(num_flips)
print(f"The highest amount of consecutive heads: {max_heads}")
print(f"The highest amount of consecutive tails: {max_tails}")
