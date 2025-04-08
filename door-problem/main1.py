import random



def create_filled_list(size):
    result = []
    good_door_index = random.randint(0, size - 1)

    for i in range(size):
        if i == good_door_index:
            result.append(True)
        else:
            result.append(False)
    return result





for i in range(0, 10):
    print(create_filled_list(3))
