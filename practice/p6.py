'''You are given a string str,you need to return True
if cat and hat appear same number of times in str, otherwise return False.'''
def cat_hat(str):
    cat_count = str.count("cat")
    hat_count = str.count("hat")
    return cat_count == hat_count

# Test the function
string = input("Enter a string: ")
result = cat_hat(string)
print("Same count of 'cat' and 'hat'?", result)
  ##your code here##
  ##You need to write complete code this time 

