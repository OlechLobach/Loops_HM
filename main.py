star_number = float(input("Enter the first number"))
end_number = float(input("Enter the second number"))
total = 0
count = 0
current_number = star_number
while current_number <= end_number:
    total += current_number
    count += 1
    current_number +=1

average = total / count
print(f"Sum of numbers in the rage: {total}")
print(f" Arithmetic mean in the rage: {average}")