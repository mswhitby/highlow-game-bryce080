x = int(input("Type a number from 1-100:"))

random_num = random.randint(1, 100)

for x in range(4):
    if random_num > x:
        x = int(input("Higher."))
    else:
        random_num < x
        x = int(input("Lower."))
else:
    if random_num == x:
        print("Correct!")
if x != random_num:
    print("Out of Attempts.")
