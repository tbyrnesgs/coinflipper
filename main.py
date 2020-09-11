import random

print("Welcome to coin flipper")

heads = 0
tails = 0

for i in range(1000):
  flip = random.randint(1,2)
  if(flip == 1):
    heads = heads + 1
  else:
    tails = tails + 1

print(f"You flipped {heads} heads")
print(f"You flipped {tails} tails")