import random
from time import time, sleep

total_time = 0
average_time = 0

print("Welcome to the reaction tester")
print("When the prompt appears hit enter")
print("Get ready!")

for attempt in range(3):
    prompt = random.random() * 5
    sleep(prompt)
    print("Quick hit the enter key!")
    start_time = time()
    input()
    reaction_time = time() - start_time
    total_time += reaction_time
    print(f"Wow that was fast it took you {reaction_time:.3f} to hit enter")

average_time = total_time / 3
print("-" * 30)
print(f"Your average time was: {average_time:.3f}")



