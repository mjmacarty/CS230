# reaction time tester

from time import sleep, time
import random
average_time = 0
total_time = 0

print("We are going to test your reaction time. I will give you five tries.")
print("When prompted press the enter key as fast as you can.")
print("Good luck!")

sleep(2)

for i in range(5):
    prompt = random.random() * 5
    print("Get ready!")
    sleep(prompt)
    start_time = time()
    
    print("Quick, press the enter key!")
    input()
    react = time() - start_time
    total_time += react
    print(f"Wow that was fast! It took you {react:.3f} seconds to press enter")

average_time = total_time/i
print("-" * 25)
print(f"Your average reaction time was {average_time:.3f} seconds" %)

    
