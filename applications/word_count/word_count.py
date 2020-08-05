import re

def word_count(s):
    # Your code here
    my_dict = {}
    # If s is empty, return empty dict
    if s == "":
        return my_dict
    # Make s lower case and split it into words
    words = s.lower()
    words = words.split()
    # Remove all characters that aren't nonalphanumeric or '
    for i, word in enumerate(words):
        words[i] = re.sub("[^a-z']+", '', word)
    unique_words = set(words)
    pairs = []
    for word in unique_words:
        pairs.append((word,words.count(word)))
    # Sort the pairs according to value
    ## Not necessary to sort
    sorted_pairs = sorted(pairs, key=lambda x:x[1], reverse=True)
    for pair in sorted_pairs:
        my_dict[pair[0]] = pair[1]
    # Delete key if it == ''
    if '' in my_dict:
        del my_dict['']

    return my_dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))