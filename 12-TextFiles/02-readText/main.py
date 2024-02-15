with open('./temp.txt','r') as file:
    # we use with structure (it automatically close the opened file) and we use read method
    content = file.read()
print(content)