'''Given a positive integer x. Your task is to check, if it is even or odd (Any number that
gives zero as remainder when divided by 2 is an even number)'''

def check_even_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = int(input("Enter a positive integer: "))
result = check_even_odd(number)
print(f"{number} is {result}.")
