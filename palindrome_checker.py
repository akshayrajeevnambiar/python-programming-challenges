# Python Code Challenge #2: Identify a Palindrome
# -----------------------------------------------
# Your goal is to implement a function, is_palindrome(), that takes a text string as the input argument and returns a boolean indicating whether or not it's a palindrome.

def is_palindrome(value):

    # STEP 1: Convert the string into lowercase and remove any spaces in between to keep the consistency
    value = value.lower().replace(' ', '')

    # STEP 2: Create pointer to check the first and the last characters
    last = len(value) - 1

    # STEP 3: return not palindrome if a mismatch occurs else its palindrome
    for i in range(0, last // 2):
        if value[i] != value[last]:
            return "Not Palindrome"

    return "Palindrome"

print(is_palindrome("Hello worLd"))
print(is_palindrome("eye"))