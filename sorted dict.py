user_input=input("enter the dictionary(eg:{'a':1,'b':2}):")
dictionary=eval(user_input)
sorted_dict=dict(sorted(dictionary.items()))
print("sorted dictionary:",sorted_dict)
