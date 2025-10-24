first_number = int(input("привет это канкуляр твоё первое число..."))
second_number = int(input("твоё второе чило..."))

choice = input("Введите операцию (+, -, *, /): , ** , %, //  " )

if choice == "+":
    result = first_number + second_number
elif choice == "**":
    result = first_number ** second_number
elif choice == "-":
    result = first_number - second_number 
elif choice == "*":
    result = first_number * second_number
elif choice == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "ошибка деление на 0"
elif choice == "%":
        result = first_number % second_number
elif choice == "//":
        result = first_number // second_number
print(f"ваш ответ , {result}")