sentence = input("Enter a sentence to see if it is a palindrome: ")


print("Is the sentence a palindrome?", sentence.lower() == sentence[::-1].lower())