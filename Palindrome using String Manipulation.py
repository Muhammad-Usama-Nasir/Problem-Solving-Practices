
def isPalindrome(str):
  string = str.lower().strip().replace(" ","")
  str_reversed = str[::-1].lower().strip().replace(" ","")
  #print(str_reversed)
  
  if string == str_reversed and len(string) == len(str_reversed):
    return True
  else:
    return False
    

def main():
  user_input = input("Enter an word, phrase or text you want to check: ")
  result = isPalindrome(user_input)
  if result:
    print("The given text is Palindrome")
  else:
    print("The given text is not Palindrome")
    
main()