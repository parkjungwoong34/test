import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)
if secret - guess > 0:
    print("too low")
elif secret - guess < 0:
    print("too high")
else:
    print("just right")

