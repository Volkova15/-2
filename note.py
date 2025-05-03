score = int(input("Введіть кількість балів (0-100): "))

if score <= 49:
    print("Оцінка: незадовільно")
elif score <= 69:
    print("Оцінка: задовільно")
elif score <= 89:
    print("Оцінка: добре")
else:
    print("Оцінка: відмінно")