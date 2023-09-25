while True:
    number = int(input("Enter the number"))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        print(f"The factorial of {number} is {factorial}.")
    продовжити =input("чи бажаєте ввести інше число? (так/ні):")
    if продовжити.lower() !='так':
         break