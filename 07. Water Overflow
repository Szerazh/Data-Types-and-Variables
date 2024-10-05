number_lines = int(input())
water_tank_capacity = 255
total_filled = 0
while number_lines > 0:
    liters_water = int(input())
    number_lines -= 1
    total_filled += liters_water
    if total_filled > water_tank_capacity:
        total_filled -= liters_water
        print(f"Insufficient capacity!")
        continue
print(f"{total_filled}")
