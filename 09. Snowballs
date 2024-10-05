number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quality = 0
for i in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    time_needed = int(input())
    quality_snowball = int(input())
    snowball_value = (snowball_weight / time_needed) ** quality_snowball
    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_time = time_needed
        max_quality = quality_snowball
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
