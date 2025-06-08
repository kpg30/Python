list = [9, 6, 4, 10, 13, 2, 3, 5]
max: int = list[0]
second_last: int = list[0]

for x in list:
    if x > max:
        second_last = max # add this line
        max = x
    elif x > second_last and x != max:
        second_last = x
print(second_last)