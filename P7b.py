import string

# Function to count the frequency of characters in a file
def count_char_frequency(filename):
    # Create an empty dictionary to store the frequency of each character
    char_frequency = {}

    # Open the file for reading
    with open(filename, 'r') as file:
        # Read the file contents and convert to lowercase
        file_contents = file.read().lower()

        # Iterate over each character in the file
        for char in file_contents:
            # Check if the character is a printable ASCII character
            if char in string.printable[:-5]:
                # Increment the frequency of the character in the dictionary
                char_frequency[char] = char_frequency.get(char, 0) + 1

    # Return the character frequency dictionary
    return char_frequency

# Function to determine whether a file is a Python program file, C program file, or a text file
def identify_file_type(filename):
    # Count the frequency of characters in the file
    char_frequency = count_char_frequency(filename)

    # Check if the file is a Python program file
    if char_frequency.get('#', 0) > char_frequency.get(';', 0):
        return 'Python program file'

    # Check if the file is a C program file
    elif char_frequency.get(';', 0) > char_frequency.get('#', 0):
        return 'C program file'

    # Otherwise, assume the file is a text file
    else:
        return 'Text file'

# Test the program with a sample file
filename = 'sample.py'
file_type = identify_file_type(filename)
print(f"The file '{filename}' is a {file_type}.")
