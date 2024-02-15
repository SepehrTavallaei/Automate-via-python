# read lines method give us all the lines in a text file in python list

with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/08-ReplaceTheFirstLine/result.csv','r') as file:
    content = file.readlines()

content[0] = 'ID,AMOUNT,COST'

with open('/Users/sepehr/Desktop/notes/PracticalLearningOfPython/12-TextFiles/08-ReplaceTheFirstLine/result.csv','w') as file:
    file.writelines(content)