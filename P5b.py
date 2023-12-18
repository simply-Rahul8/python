class StringReverser:
    def __init__(self):
        self.string = input("Enter a string: ")
    
    def reverse_words(self):
        # split the string into words
        words = self.string.split()

        # reverse the order of the words
        words = words[::-1]

        # join the words back into a string
        reversed_string = " ".join(words)

        return reversed_string
reverser = StringReverser()
print(reverser.reverse_words())
