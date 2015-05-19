def isPalindrome(digits):
        if list(digits) == list(reversed(digits)):
           return True
        return False

digits = input("Enter any number or character: ")
if isPalindrome(digits):
   print ("%s is a palindrome"%(digits))
else:
   print ("%s is not a palindrome"%(digits))
