import random

def test():
    return random.randint(0, 2)

goaaaaal = 0
not_goaaaaal = 0

goaaaaal_alt = 0
not_goaaaaal_alt = 0

doors = [1, 0, 0]



for x in range(1000):
    choice_index = random.randint(0, 2)

    first_choice = doors[choice_index]

    for i in range(len(doors)):
        if i == choice_index:
            continue

        if doors[i] == 0:
            bad_door_index = i
            break

    if doors[choice_index] == 1:
        goaaaaal += 1
    else:
        not_goaaaaal += 1


for x in range(1000):
    choice_index = random.randint(0, 2)

    first_choice = doors[choice_index]

    for i in range(len(doors)):
        if i == choice_index:
            continue

        if doors[i] == 0:
            bad_door_index = i
            break


    new_choice_index = test()
    while(new_choice_index == bad_door_index or new_choice_index == choice_index):
        new_choice_index = test()

    if doors[new_choice_index] == 1:
        goaaaaal_alt += 1
    else:
        not_goaaaaal_alt += 1


print("не поменяли выбор:")
print("ты забил гол " + str(goaaaaal) + " раз")
print("ты дал в жопу " + str(not_goaaaaal) + " раз")

print("поменяли выбор:")
print("ты забил гол " + str(goaaaaal_alt) + " раз")
print("ты дал в жопу " + str(not_goaaaaal_alt) + " раз")







