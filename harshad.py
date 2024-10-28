num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))
is_harshad = num % digit_sum == 0
print("Harshad" if is_harshad else "Not Harshad")
