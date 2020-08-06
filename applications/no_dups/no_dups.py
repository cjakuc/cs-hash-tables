def no_dups(s):
    # Your code here
    if s == "":
        return ""
    my_dict = {}
    for word in s.split():
        my_dict[word] = ""
    msg = list(my_dict.keys())[0]
    if len(list(my_dict.keys())) > 1:
        for word in list(my_dict.keys())[1:]:
            msg += f" {word}"
    return msg



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))