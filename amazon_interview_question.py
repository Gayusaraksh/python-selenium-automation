# def first_unique_letter(word):
#     unique_char = []
#     for i in word:
#         if i not in unique_char:
#             if word.count(i) == 1:
#                 return i
#             else:
#                 unique_char.append(i)
#     return""
#
#
# first_unique_letter('google')

def first_unique_letter(s):
    # Create a list to store the unique characters
    unique_chars = []
    # Loop through each character in the string
    for char in s:
        # If the character is not already in the list of unique characters
        if char not in unique_chars:
            # Check if the character is unique
            if s.count(char) == 1:
                # If the character is unique, return it
                print(char)
            else:
                # If the character is not unique, add it to the list of unique characters
                unique_chars.append(char)
    # If no unique characters are found, return an empty string
    return ""


first_unique_letter('google')
