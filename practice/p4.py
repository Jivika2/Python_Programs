'''You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive,
print numbers from n-1 to 0 by subtracting 1 from n in the pos function.'''

def pos(n):
    if n <= 0:
        print("The number is negative. Use neg() function instead.")
        return
    while n >= 0:
        print(n)
        n -= 1
    
        
    
def neg(n):
    if n >= 0:
        print("The number is positive. Use pos() function instead.")
        return
    while n <= 0:
        print(n)
        n += 1
number = int(input("Enter a number: "))
if number < 0:
    neg(number)
else:
    pos(number)
    
