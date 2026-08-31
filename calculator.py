language = input("اختر اللغة / Choose language (عربي / English): ").strip().lower()

if language in ["عربي", "العربية", "arabic"]:
    first_message = "أدخل الرقم الأول: "
    operator_message = "أدخل العملية (+, -, *, /): "
    second_message = "أدخل الرقم الثاني: "
    invalid_operator = "عملية غير صحيحة"
    divide_zero = "لا يمكن القسمة على صفر"
    result_message = "النتيجة: "

else:
    first_message = "Enter first number: "
    operator_message = "Enter operator (+, -, *, /): "
    second_message = "Enter second number: "
    invalid_operator = "Invalid operator"
    divide_zero = "Cannot divide by zero"
    result_message = "Result: "

num1 = float(input(first_message))
operator = input(operator_message)
num2 = float(input(second_message))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = divide_zero

else:
    result = invalid_operator

print(result_message, result)
