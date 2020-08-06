# Your code here

# Read in all the words in one go
with open(r"applications\histo\robin.txt") as f:
    words = f.read()

my_dict = {}

# Remove unwanted characters
to_remove = '":;,.-+=/\|[]{(})*^&'
for char in to_remove:
    words = words.replace(char, "")

# Make words lower case and split it into words
words = words.lower()
words = words.split()

# Add words and count to my_dict
## Find the longest word
longest = 0
for word in words:
    if word not in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] += 1
    if len(word) > longest:
        longest = len(word)

# Sort the words according to count then alphabetically
sorted_counts = sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))

# Print each word w/ correct number of spaces and "#"s
for word in sorted_counts:
    spaces = " "*(longest - len(word[0]))
    count = "#"*word[1]
    print(f"{word[0]}{spaces}{count}")