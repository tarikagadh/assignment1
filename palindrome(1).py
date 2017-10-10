inputStr = input("Enter a string: ")

def isPalindrome(s):
    index = 0 
    check = True
    while index<len(s): #length of word is greater than 0
        if s[index]==s[-1-index]: #word is same when it is reversed
            index+-1
            return True
        return False

if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")




