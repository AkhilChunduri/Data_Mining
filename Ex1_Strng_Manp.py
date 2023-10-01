greet = "Hello work"
extended_grt = "Hello World, " + "this is a long string"
name = "John"
intruption = f"Hello {name}"
greet_format = "Hello {}"

#String interpolation
formatted = greet_format.format(name)

print(intruption, formatted)
print(formatted.upper()) #String Case Conversion:
print(formatted.lower()) #String Case Conversion:
print(formatted.replace("John","Akhil")) #String replace

#another example of string interpolation
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)

#String concatanation
first_name = "Akhil"
last_name = "Gupta"
full_name = first_name + " " + last_name
print("String Concanation of 2 names is "+full_name)

#String Length
text = "Python is great!"
length = len(text)  # Returns 16
print(length)

#String splitting
sentence = "This is a sample sentence."
words = sentence.split(" ")  # Splits into a list of words
print(words)

#String Stripping
text2 = "   Some text with spaces    "
cleaned_text = text2.strip()
right_strip = text2.rstrip()
left_strip = text2.lstrip()
print(cleaned_text + "\n" + right_strip + "\n" + left_strip)

#String searching
text3 = "Searching for a keyword in this text."
position = text3.find("keyword")  # Returns the index where "keyword" starts
string_index = text3.index("t")
print("String searching")
print(position)
print(string_index)

#String Validation
username = "user123"
is_alpha_numeric = username.isalnum()  # Checks if the string contains only letters and digits
print("String Validation")
print("Is Alpha Numerice" + is_alpha_numeric)
