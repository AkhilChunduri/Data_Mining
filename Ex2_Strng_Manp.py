#String Transformation

#String Splitting and Joining
text="Data engineers often need to perform various string transformations and validations."
split_text =  text.split(" ")
print(split_text)
joined_text = " ".join(split_text)
print(joined_text)

#String Truncation
text = "This is a long string that needs to be truncated."
truncated_text = text[:20]  # Truncate to 20 characters
print(truncated_text)

#String Padding
#Adding characters (usually spaces) to the beginning or 
# end of a string to make it a specific length.
Text = "123"
padded_text = text.rjust(5, "0")  # Right-justify with zeros to make it 5 characters long
print(padded_text)

#String Regular Expressions
import re
TEXT = "Date: 2023-09-30"
PATTERN = r"\d{4}-\d{2}-\d{2}"
match = re.search(PATTERN, TEXT)  # Extracts the date
if match:
    date_parts = match.group().split("-")
    formatted_date = f"{date_parts[1]}-{date_parts[2][-2:]}-{date_parts[0][-2:]}"
    print(formatted_date)
else:
    print("Date not found.")


#String Validation
#Numeric Validation: Checking if a string represents a valid number (integer or floating-point).
num_str = "A123"
print(num_str.isdigit())

#Email Validation
email = "user@example.com"
is_valid_email = bool(re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", email))
if is_valid_email:
    print("Email is Valid: " + email)

#Custome Validation
DATA = input("Enter a 5 digit number: ") #Take input from user
is_valid = len(DATA) == 5 and DATA.isdigit()
if is_valid:
    print("DATA is having 5 digits")
    