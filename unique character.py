def unique_character(input_string):
    cleaned_string=string.replace(" ","").lower()
    set_char=set()

    for char in cleaned_string:
        if char in set_char:
            return False
        set_char.add(char)
    return True
    
string=input("enter the string:")
print(unique_character(string))
