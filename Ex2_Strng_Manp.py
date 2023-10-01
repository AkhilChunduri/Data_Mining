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

