import random

unique_numbers = set()

while len(unique_numbers) < 1000:
    unique_numbers.add(random.randint(0, 4999))

unique_numbers_list = list(unique_numbers)  # Convert set to list if needed
#unique_numbers_list.sort()
for i in unique_numbers_list:
    print(random.randint(0, 4999))