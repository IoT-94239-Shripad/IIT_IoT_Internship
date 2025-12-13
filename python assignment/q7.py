
num = input("Enter a 5-digit number: ")
if num.isdigit() and len(num) == 5:  
    rev = num[::-1]
    if num == rev:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Error: Please enter a valid 5-digit number.")
