#Problem 1: User Profile Generator
first_name =input("What is your first name?")
last_name = input("What is your last name?")
hobby = input("What is your favorite hobby?")
birth_year = input("What is your Birth Year?")

print("=========================\n", "Profile Card\n", "=========================")
print("Name:", first_name, last_name)
print("Hobby:", hobby)
print("Age: ", 2026 - int(birth_year))
print("=========================")
print("Your Profile Card has been created successfully!")

#Problem 2: Text Analyzer
sentence = input("Enter a sentence: ")

print("Number of characters:", len(sentence))
print("Number of characters without spaces:", len(sentence.replace(" ", "")))
print("Number of words:", len(sentence.split()))
print("Number of vowels:", sum(1 for char in sentence if char.lower() in 'aeiou'))
print("Reversed sentence:", sentence[::-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Ends with punctuation:", sentence[-1] in '.,!?')
print("Starts withCapital:", sentence[0].isupper())


#Bonus Problem 3: Palindrome Checker
sentence2 = input("Enter a sentence to see if it is a palindrome: ")


print("Is the sentence a palindrome?", sentence2.lower() == sentence2[::-1].lower())