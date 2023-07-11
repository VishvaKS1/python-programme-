def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    return number == reversed_number

def count_digits(number):
    return len(str(number))

def main():
    n = int(input("Enter an integer: "))

    if n % 2 == 1:  
        fact = factorial(n)
        digit_count = count_digits(fact)
        print(f"The factorial of {n} is: {fact}")
        print(f"The number of digits in the factorial of {n} is: {digit_count}")
    else:  
        if is_palindrome(n):
            print("the number is even")
            print(f"The number {n} is a palindrome.")
          
        else:
            print("the number is even")
            print(f"The number {n} is not a palindrome.")

main()
