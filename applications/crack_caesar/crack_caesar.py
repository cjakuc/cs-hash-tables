# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("applications\crack_caesar\ciphertext.txt") as f:
    words = f.read()

my_dict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nat_freq = "ETAOHNRISDLWUGFBMYCPKVQJXZ"
# Make my_dict k,v = letter: count
for letter in alphabet:
    my_dict[letter] = words.count(letter)
# Get a list of letter sorted by frequency
sorted_counts = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
# Make the values for my_dict = X most common letter in natural English according to their observed frequency in the text
for i, item in enumerate(sorted_counts):
    my_dict[item[0]] = nat_freq[i]

# Loop through the cipher text and decipher it
output = ""
for letter in words:
    if letter in list(my_dict.keys()):
        output += my_dict[letter]
    else:
        output += letter
print(output)