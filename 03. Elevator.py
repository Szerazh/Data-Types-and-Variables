from math import ceil
num_persons = int(input())
capacity_elevator = int(input())
num_times = ceil(num_persons / capacity_elevator)
print(num_times)
